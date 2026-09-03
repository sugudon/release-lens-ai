from backend.app.retrieval.factory import (
    create_retriever,
)


def main():

    question = (
        "What could be affected by "
        "changing payment retry behavior?"
    )

    retriever = create_retriever(
        top_k=5,
    )

    documents = retriever.invoke(
        question
    )

    print(
        f"\nQuestion:\n{question}\n"
    )

    print(
        f"Retrieved {len(documents)} documents\n"
    )

    for index, document in enumerate(
        documents,
        start=1,
    ):
        print("=" * 70)

        print(
            f"Result {index}"
        )

        print(
            "Document ID:",
            document.metadata["document_id"],
        )

        print(
            "Chunk ID:",
            document.metadata["chunk_id"],
        )

        print(
            "Type:",
            document.metadata["document_type"],
        )

        print(
            "Service:",
            document.metadata["service"],
        )

        print(
            "Distance:",
            document.metadata["distance"],
        )

        print(
            "\nContent:"
        )

        print(
            document.page_content
        )


if __name__ == "__main__":
    main()