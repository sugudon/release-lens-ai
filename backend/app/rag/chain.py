from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from backend.app.models.release_analysis import (
    ReleaseAnalysis,
)

from backend.app.rag.prompts import (
    RELEASE_ANALYSIS_PROMPT,
)

from backend.app.retrieval.factory import (
    create_retriever,
)


def format_documents(
    documents: list[Document],
) -> str:

    if not documents:
        return (
            "No relevant engineering evidence was retrieved."
        )

    formatted_documents = []

    for document in documents:

        metadata = document.metadata

        document_id = metadata.get(
            "document_id",
            "UNKNOWN",
        )

        document_type = metadata.get(
            "document_type",
            "UNKNOWN",
        )

        service = metadata.get(
            "service",
            "UNKNOWN",
        )

        source = metadata.get(
            "source",
            "UNKNOWN",
        )

        formatted_documents.append(
            f"""
[DOCUMENT]
document_id: {document_id}
document_type: {document_type}
service: {service}
source: {source}

content:
{document.page_content}
[/DOCUMENT]
"""
        )

    return "\n".join(formatted_documents)

def create_rag_chain():

    retriever = create_retriever(
        top_k=5,
    )

    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    structured_model = model.with_structured_output(
        ReleaseAnalysis
    )

    chain = (
        {
            "context": (
                RunnableLambda(
                    lambda x: x["release_description"]
                )
                | retriever
                | format_documents
            ),
            "release_description": RunnableLambda(
                lambda x: x["release_description"]
            ),
        }
        | RELEASE_ANALYSIS_PROMPT
        | structured_model
    )

    return chain