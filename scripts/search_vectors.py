from backend.app.db.search import (
    similarity_search,
)

from backend.app.ingestion.embeddings import (
    embed_query,
)


def main():
    query = (
        "What caused the previous "
        "payment timeout?"
    )

    query_vector = embed_query(query)

    results = similarity_search(
        query_vector,
        limit=5,
        document_type="incident",
    )

    print(
        f"\nQuery: {query}\n"
    )

    for index, result in enumerate(
        results,
        start=1,
    ):
        print(
            f"\nResult {index}"
        )

        print(
            "Document:",
            result["document_id"],
        )

        print(
            "Chunk:",
            result["chunk_id"],
        )

        print(
            "Type:",
            result["document_type"],
        )

        print(
            "Service:",
            result["service"],
        )

        print(
            "Distance:",
            result["distance"],
        )

        print(
            "Content:",
            result["content"],
        )


if __name__ == "__main__":
    main()