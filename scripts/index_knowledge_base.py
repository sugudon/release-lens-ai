from backend.app.db.vector_store import (
    insert_chunk,
)

from backend.app.ingestion.embeddings import (
    embed_documents,
)

from backend.app.ingestion.loader import (
    load_knowledge_base,
)

from backend.app.ingestion.splitter import (
    split_documents,
)


def main():
    documents = load_knowledge_base()

    chunks = split_documents(
        documents,
        chunk_size=800,
        chunk_overlap=120,
    )

    vectors = embed_documents(chunks)

    for chunk, vector in zip(chunks, vectors):
        metadata = chunk.metadata

        insert_chunk(
            document_id=metadata["document_id"],
            chunk_id=metadata["chunk_id"],
            document_type=metadata["document_type"],
            service=metadata.get("service"),
            source=metadata["source"],
            status=metadata.get("status"),
            content=chunk.page_content,
            embedding=vector,
        )

    print(
        f"Indexed {len(chunks)} chunks."
    )


if __name__ == "__main__":
    main()