from dataclasses import dataclass


@dataclass
class ProcessedQuery:
    original_query: str
    retrieval_query: str
    concepts: list[str]


def process_query(
    query: str,
) -> ProcessedQuery:

    normalized_query = query.strip()

    if not normalized_query:
        return ProcessedQuery(
            original_query=query,
            retrieval_query="",
            concepts=[],
        )

    concepts = []

    query_lower = normalized_query.lower()

    # ---------------------------------------------
    # Payment
    # ---------------------------------------------

    if "payment" in query_lower:

        concepts.extend(
            [
                "payment",
                "payment API",
                "payment service",
            ]
        )

    # ---------------------------------------------
    # Retry
    # ---------------------------------------------

    if "retry" in query_lower:

        concepts.extend(
            [
                "retry",
                "retry configuration",
                "payment retry",
            ]
        )

    # ---------------------------------------------
    # Timeout
    # ---------------------------------------------

    if (
        "retry" in query_lower
        or "timeout" in query_lower
    ):

        concepts.extend(
            [
                "payment timeout",
                "timeout incident",
            ]
        )

    # ---------------------------------------------
    # Checkout
    # ---------------------------------------------

    if "checkout" in query_lower:

        concepts.append(
            "checkout"
        )

    # ---------------------------------------------
    # API
    # ---------------------------------------------

    if "api" in query_lower:

        concepts.extend(
            [
                "API",
                "API dependency",
            ]
        )

    # ---------------------------------------------
    # Remove duplicates
    # ---------------------------------------------

    concepts = list(
        dict.fromkeys(concepts)
    )

    # ---------------------------------------------
    # Build retrieval query
    # ---------------------------------------------

    retrieval_query = " ".join(
        [normalized_query] + concepts
    )

    return ProcessedQuery(
        original_query=normalized_query,
        retrieval_query=retrieval_query,
        concepts=concepts,
    )