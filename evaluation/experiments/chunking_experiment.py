from statistics import mean

from backend.app.ingestion.loader import (
    load_knowledge_base,
)

from backend.app.ingestion.splitter import (
    split_documents,
)


CONFIGURATIONS = [
    {
        "name": "A",
        "chunk_size": 500,
        "chunk_overlap": 75,
    },
    {
        "name": "B",
        "chunk_size": 1000,
        "chunk_overlap": 150,
    },
]


def calculate_statistics(chunks):
    lengths = [
        len(chunk.page_content)
        for chunk in chunks
    ]

    return {
        "chunk_count": len(chunks),
        "average_length": round(mean(lengths), 2),
        "min_length": min(lengths),
        "max_length": max(lengths),
    }


def run_experiment(documents, config):
    chunks = split_documents(
        documents,
        chunk_size=config["chunk_size"],
        chunk_overlap=config["chunk_overlap"],
    )

    statistics = calculate_statistics(chunks)

    return {
        **config,
        **statistics,
    }


def main():
    documents = load_knowledge_base()

    print(
        f"Original documents: {len(documents)}"
    )

    for config in CONFIGURATIONS:
        result = run_experiment(
            documents,
            config,
        )

        print("\n==============================")
        print(
            f"Experiment {result['name']}"
        )
        print("==============================")

        print(
            f"Chunk size: "
            f"{result['chunk_size']}"
        )

        print(
            f"Chunk overlap: "
            f"{result['chunk_overlap']}"
        )

        print(
            f"Chunk count: "
            f"{result['chunk_count']}"
        )

        print(
            f"Average length: "
            f"{result['average_length']}"
        )

        print(
            f"Minimum length: "
            f"{result['min_length']}"
        )

        print(
            f"Maximum length: "
            f"{result['max_length']}"
        )


if __name__ == "__main__":
    main()