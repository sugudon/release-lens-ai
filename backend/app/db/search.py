from sqlalchemy import text

from backend.app.db.connection import engine


def similarity_search(
    query_vector,
    limit=5,
    document_type=None,
):
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

    if document_type:
        query_string += """
            WHERE document_type = :document_type
        """

        parameters["document_type"] = document_type

    query_string += """
        ORDER BY embedding <=> CAST(:query_vector AS vector)
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