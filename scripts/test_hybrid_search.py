from backend.app.db.keyword_search import (
    keyword_search,
)

from backend.app.db.search import (
    similarity_search,
)

from backend.app.ingestion.embeddings import (
    embed_query,
)

from backend.app.retrieval.hybrid_search import (
    hybrid_search,
)


def print_results(
    title,
    documents,
):
    print("\n")
    print("=" * 80)
    print(title)
    print("=" * 80)

    for index, document in enumerate(
        documents,
        start=1,
    ):

        if hasattr(document, "metadata"):
            metadata = document.metadata
            content = document.page_content

        else:
            metadata = document
            content = document["content"]

        print(
            f"""
Rank:
{index}

Document:
{metadata.get("document_id")}

Type:
{metadata.get("document_type")}

Service:
{metadata.get("service")}

Source:
{metadata.get("source")}

Content:
{content[:250]}
"""
        )


def test_query(query):

    print("\n")
    print("#" * 80)
    print(f"QUERY: {query}")
    print("#" * 80)

    # -------------------------------------------------
    # Semantic
    # -------------------------------------------------

    query_vector = embed_query(query)

    semantic_results = similarity_search(
        query_vector=query_vector,
        limit=5,
    )

    print_results(
        "SEMANTIC SEARCH",
        semantic_results,
    )

    # -------------------------------------------------
    # Keyword
    # -------------------------------------------------

    keyword_results = keyword_search(
        query=query,
        limit=5,
    )

    print_results(
        "KEYWORD SEARCH",
        keyword_results,
    )

    # -------------------------------------------------
    # Hybrid
    # -------------------------------------------------

    hybrid_results = hybrid_search(
        query=query,
        limit=5,
    )

    print_results(
        "HYBRID SEARCH",
        hybrid_results,
    )


def main():

    queries = [
        "INC-1024",
        "ADR-003",
        "What caused payment timeout problems?",
        "HTTP 504 payment timeout",
    ]

    for query in queries:
        test_query(query)


if __name__ == "__main__":
    main() 