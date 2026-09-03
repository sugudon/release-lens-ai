from sqlalchemy import text

from backend.app.db.connection import engine


def similarity_search(
    query_vector,
    limit=5,
    document_type=None,
    service=None,
):
    """
    Perform vector similarity search with optional
    metadata filtering.

    Args:
        query_vector: Query embedding vector.
        limit: Maximum number of results.
        document_type: Optional metadata filter.
        service: Optional metadata filter.

    Returns:
        List of matching document chunks.
    """

    query_string = """
        SELECT
            id,
            document_id,
            chunk_id,
            document_type,
            service,
            source,
            status,
            content,
            embedding <=> CAST(:query_vector AS vector)
                AS distance
        FROM document_chunks
    """

    parameters = {
        "query_vector": str(query_vector),
        "limit": limit,
    }

    # =====================================================
    # Metadata Filters
    # =====================================================

    filters = []

    # -----------------------------------------------------
    # Filter by document type
    # -----------------------------------------------------

    if document_type:
        filters.append(
            "document_type = :document_type"
        )

        parameters["document_type"] = (
            document_type
        )

    # -----------------------------------------------------
    # Filter by service
    # -----------------------------------------------------

    if service:
        filters.append(
            "service = :service"
        )

        parameters["service"] = service

    # -----------------------------------------------------
    # Build WHERE clause
    # -----------------------------------------------------

    if filters:
        query_string += "\nWHERE "

        query_string += "\nAND ".join(
            filters
        )

    # =====================================================
    # Vector Similarity Ordering
    # =====================================================

    query_string += """
        ORDER BY embedding <=> CAST(:query_vector AS vector)
        LIMIT :limit
    """

    # =====================================================
    # Execute Query
    # =====================================================

    query = text(query_string)

    with engine.connect() as connection:

        results = connection.execute(
            query,
            parameters,
        )

        return [
            dict(row._mapping)
            for row in results
        ]