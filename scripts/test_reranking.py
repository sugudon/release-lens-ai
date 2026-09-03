from backend.app.retrieval.hybrid_search import (
    hybrid_search,
)

from backend.app.retrieval.reranker import (
    ReleaseLensReranker,
)


def main():

    query = (
        "What could be affected by "
        "changing payment retry behavior?"
    )

    # ---------------------------------------------
    # Initial retrieval
    # ---------------------------------------------

    candidates = hybrid_search(
        query=query,
        limit=20,
    )

    print("\n")
    print("=" * 80)
    print("INITIAL RETRIEVAL")
    print("=" * 80)

    for index, document in enumerate(
        candidates,
        start=1,
    ):

        print(
            f"{index}. "
            f"{document.metadata.get('document_id')} "
            f"| "
            f"{document.metadata.get('document_type')}"
        )

    # ---------------------------------------------
    # Reranking
    # ---------------------------------------------

    reranker = ReleaseLensReranker()

    reranked_documents = (
        reranker.rerank(
            query=query,
            documents=candidates,
            top_k=5,
        )
    )

    print("\n")
    print("=" * 80)
    print("RERANKED RESULTS")
    print("=" * 80)

    for index, document in enumerate(
        reranked_documents,
        start=1,
    ):

        print(
            f"{index}. "
            f"{document.metadata.get('document_id')} "
            f"| "
            f"rerank_score="
            f"{document.metadata.get('rerank_score')}"
        )


if __name__ == "__main__":
    main()