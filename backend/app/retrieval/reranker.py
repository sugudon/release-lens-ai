from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from backend.app.models.reranking import (
    RerankResult,
)


RERANK_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a relevance-ranking component
for an engineering knowledge retrieval system.

Your task is to rank retrieved engineering
documents against a user query.

Evaluate relevance based on:

- Direct relationship to the query
- Service/component relevance
- Technical context
- Evidence usefulness

Do not invent information.

Return only the structured ranking result.
""",
        ),
        (
            "human",
            """
USER QUERY:

{query}

CANDIDATE DOCUMENTS:

{documents}
""",
        ),
    ]
)


class ReleaseLensReranker:

    def __init__(
        self,
        model_name: str = "gpt-4.1-mini",
    ):

        model = ChatOpenAI(
            model=model_name,
            temperature=0,
        )

        self.model = (
            model.with_structured_output(
                RerankResult
            )
        )

    def rerank(
        self,
        query: str,
        documents: list[Document],
        top_k: int = 5,
    ) -> list[Document]:

        if not documents:
            return []

        formatted_documents = []

        for document in documents:

            metadata = document.metadata

            formatted_documents.append(
                f"""
DOCUMENT

document_id:
{metadata.get("document_id")}

chunk_id:
{metadata.get("chunk_id")}

document_type:
{metadata.get("document_type")}

service:
{metadata.get("service")}

content:
{document.page_content}

END DOCUMENT
"""
            )

        document_text = "\n".join(
            formatted_documents
        )

        ranking_result = (
            RERANK_PROMPT
            | self.model
        ).invoke(
            {
                "query": query,
                "documents": document_text,
            }
        )

        scores = {
            (
                item.document_id,
                item.chunk_id,
            ): item.relevance_score
            for item in ranking_result.results
        }

        ranked_documents = []

        for document in documents:

            key = (
                document.metadata.get(
                    "document_id"
                ),
                document.metadata.get(
                    "chunk_id"
                ),
            )

            if key not in scores:
                continue

            document.metadata[
                "rerank_score"
            ] = scores[key]

            ranked_documents.append(
                document
            )

        ranked_documents.sort(
            key=lambda document:
                document.metadata[
                    "rerank_score"
                ],
            reverse=True,
        )

        return ranked_documents[:top_k]