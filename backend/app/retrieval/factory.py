from backend.app.retrieval.retriever import (
    ReleaseLensRetriever,
)


def create_retriever(
    *,
    top_k: int = 5,
    similarity_threshold: float | None = None,
    document_type: str | None = None,
    service: str | None = None,
):
    return ReleaseLensRetriever(
        top_k=top_k,
        similarity_threshold=similarity_threshold,
        document_type=document_type,
        service=service,
    )