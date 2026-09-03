from backend.app.ingestion.loader import (
    load_knowledge_base,
)

from backend.app.ingestion.splitter import (
    split_documents,
)

from langchain_core.documents import Document



def test_documents_are_split():
    documents = load_knowledge_base()

    chunks = split_documents(
        documents,
        chunk_size=500,
        chunk_overlap=75,
    )

    assert len(chunks) > len(documents)


def test_chunk_metadata_is_preserved():
    documents = load_knowledge_base()

    chunks = split_documents(
        documents,
        chunk_size=500,
        chunk_overlap=75,
    )

    for chunk in chunks:
        assert chunk.metadata["document_id"]
        assert chunk.metadata["document_type"]
        assert chunk.metadata["service"]
        assert chunk.metadata["source"]
        assert chunk.metadata["chunk_id"]


def test_chunk_size_is_respected():
    documents = load_knowledge_base()

    chunks = split_documents(
        documents,
        chunk_size=500,
        chunk_overlap=75,
    )

    for chunk in chunks:
        assert len(chunk.page_content) <= 500

def test_overlap_configuration():
    document = Document(
        page_content=(
            "A " * 200
        ),
        metadata={
            "document_id": "TEST-001",
            "document_type": "test",
            "service": "test-service",
            "source": "test",
            "status": "active",
        },
    )

    chunks = split_documents(
        [document],
        chunk_size=100,
        chunk_overlap=20,
    )

    assert len(chunks) > 1