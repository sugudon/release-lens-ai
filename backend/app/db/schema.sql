CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS document_chunks (
    id BIGSERIAL PRIMARY KEY,

    document_id VARCHAR(128) NOT NULL,

    chunk_id VARCHAR(256) NOT NULL UNIQUE,

    document_type VARCHAR(64) NOT NULL,

    service VARCHAR(128),

    source TEXT NOT NULL,

    status VARCHAR(64),

    content TEXT NOT NULL,

    embedding VECTOR(1536) NOT NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);


CREATE INDEX IF NOT EXISTS idx_document_chunks_document_id
ON document_chunks(document_id);

CREATE INDEX IF NOT EXISTS idx_document_chunks_document_type
ON document_chunks(document_type);

CREATE INDEX IF NOT EXISTS idx_document_chunks_service
ON document_chunks(service);

CREATE INDEX IF NOT EXISTS idx_document_chunks_embedding_hnsw
ON document_chunks
USING hnsw (embedding vector_cosine_ops);