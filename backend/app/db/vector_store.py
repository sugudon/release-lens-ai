from sqlalchemy import text

from backend.app.db.connection import engine


def insert_chunk(
    *,
    document_id,
    chunk_id,
    document_type,
    service,
    source,
    status,
    content,
    embedding,
):
    query = text(
        """
        INSERT INTO document_chunks (
            document_id,
            chunk_id,
            document_type,
            service,
            source,
            status,
            content,
            embedding
        )
        VALUES (
            :document_id,
            :chunk_id,
            :document_type,
            :service,
            :source,
            :status,
            :content,
            CAST(:embedding AS vector)
        )
        ON CONFLICT (chunk_id)
        DO NOTHING
        """
    )

    with engine.begin() as connection:
        connection.execute(
            query,
            {
                "document_id": document_id,
                "chunk_id": chunk_id,
                "document_type": document_type,
                "service": service,
                "source": source,
                "status": status,
                "content": content,
                "embedding": str(embedding),
            },
        )