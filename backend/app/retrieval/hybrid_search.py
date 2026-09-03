from collections import defaultdict

from langchain_core.documents import Document

from backend.app.db.search import similarity_search
from backend.app.db.keyword_search import keyword_search
from backend.app.ingestion.embeddings import embed_query


def hybrid_search(
    query: str,
    limit: int = 20,
    document_type: str | None = None,
    service: str | None = None,
):
    """
    Combine semantic vector search and keyword search
    using Reciprocal Rank Fusion.
    """

    # =================================================
    # Semantic Search
    # =================================================

    query_vector = embed_query(query)

    semantic_results = similarity_search(
        query_vector=query_vector,
        limit=limit,
        document_type=document_type,
        service=service,
    )

    # =================================================
    # Keyword Search
    # =================================================

    keyword_results = keyword_search(
        query=query,
        limit=limit,
        document_type=document_type,
        service=service,
    )

    # =================================================
    # Reciprocal Rank Fusion
    # =================================================

    rrf_k = 60

    scores = defaultdict(float)
    documents = {}

    # -------------------------------------------------
    # Semantic ranking
    # -------------------------------------------------

    for rank, result in enumerate(
        semantic_results,
        start=1,
    ):

        document_id = result["document_id"]
        chunk_id = result["chunk_id"]

        key = (
            document_id,
            chunk_id,
        )

        scores[key] += (
            1 / (rrf_k + rank)
        )

        documents[key] = result

    # -------------------------------------------------
    # Keyword ranking
    # -------------------------------------------------

    for rank, result in enumerate(
        keyword_results,
        start=1,
    ):

        document_id = result["document_id"]
        chunk_id = result["chunk_id"]

        key = (
            document_id,
            chunk_id,
        )

        scores[key] += (
            1 / (rrf_k + rank)
        )

        if key not in documents:
            documents[key] = result

    # =================================================
    # Sort Combined Results
    # =================================================

    ranked_keys = sorted(
        scores,
        key=scores.get,
        reverse=True,
    )

    # =================================================
    # Convert to LangChain Documents
    # =================================================

    final_documents = []

    for key in ranked_keys[:limit]:

        result = documents[key]

        final_documents.append(
            Document(
                page_content=result["content"],

                metadata={
                    "document_id":
                        result["document_id"],

                    "chunk_id":
                        result["chunk_id"],

                    "document_type":
                        result["document_type"],

                    "service":
                        result["service"],

                    "source":
                        result["source"],

                    "status":
                        result["status"],

                    "hybrid_score":
                        scores[key],
                },
            )
        )

    return final_documents