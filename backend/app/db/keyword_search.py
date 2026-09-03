from sqlalchemy import text

from backend.app.db.connection import engine


def keyword_search(
    query,
    limit=5,
    document_type=None,
    service=None,
):
    """
    Perform PostgreSQL full-text keyword search
    with optional metadata filtering.
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

            ts_rank(
                to_tsvector(
                    'english',
                    content
                ),
                plainto_tsquery(
                    'english',
                    :query
                )
            ) AS keyword_score

        FROM document_chunks
    """

    parameters = {
        "query": query,
        "limit": limit,
    }

    filters = []

    # ---------------------------------------------
    # Metadata filters
    # ---------------------------------------------

    if document_type:
        filters.append(
            "document_type = :document_type"
        )

        parameters["document_type"] = (
            document_type
        )

    if service:
        filters.append(
            "service = :service"
        )

        parameters["service"] = service

    # ---------------------------------------------
    # Apply filters
    # ---------------------------------------------

    if filters:
        query_string += "\nWHERE "
        query_string += "\nAND ".join(filters)

    # ---------------------------------------------
    # Keyword relevance
    # ---------------------------------------------

    query_string += """
        ORDER BY keyword_score DESC
        LIMIT :limit
    """

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