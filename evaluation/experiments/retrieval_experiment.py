from backend.app.retrieval.factory import (
    create_retriever,
)


QUESTIONS = [
    "What could be affected by changing payment retry behavior?",
    "What caused the previous payment timeout?",
    "What testing is required for payment retry changes?",
]


CONFIGURATIONS = [
    {
        "top_k": 3,
        "similarity_threshold": None,
    },
    {
        "top_k": 5,
        "similarity_threshold": None,
    },
    {
        "top_k": 5,
        "similarity_threshold": 0.40,
    },
]


def main():

    for configuration in CONFIGURATIONS:

        print("\n")
        print("=" * 70)

        print(
            "Configuration:",
            configuration,
        )

        retriever = create_retriever(
            **configuration
        )

        for question in QUESTIONS:

            documents = retriever.invoke(
                question
            )

            print("\nQuestion:")
            print(question)

            print(
                "Retrieved:",
                len(documents),
            )

            for document in documents:

                print(
                    "-",
                    document.metadata[
                        "document_id"
                    ],
                    "| distance:",
                    document.metadata[
                        "distance"
                    ],
                )


if __name__ == "__main__":
    main()