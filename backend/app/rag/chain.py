from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from backend.app.rag.prompts import RELEASE_ANALYSIS_PROMPT
from backend.app.retrieval.factory import create_retriever


def format_documents(documents: list[Document]) -> str:

    if not documents:
        return "No relevant engineering evidence was retrieved."

    formatted_documents = []

    for document in documents:

        document_id = document.metadata.get(
            "document_id",
            "UNKNOWN",
        )

        document_type = document.metadata.get(
            "document_type",
            "UNKNOWN",
        )

        service = document.metadata.get(
            "service",
            "UNKNOWN",
        )

        source = document.metadata.get(
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
        | model
        | StrOutputParser()
    )

    return chain