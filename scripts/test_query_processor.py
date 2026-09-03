from backend.app.retrieval.query_processor import (
    process_query,
)


def main():

    query = "payment retry issue"

    result = process_query(query)

    print("Original:")
    print(result.original_query)

    print("\nConcepts:")
    for concept in result.concepts:
        print(f"- {concept}")

    print("\nRetrieval Query:")
    print(result.retrieval_query)


if __name__ == "__main__":
    main()