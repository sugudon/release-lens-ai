from backend.app.ingestion.loader import load_knowledge_base


def test_knowledge_base_loads():
    documents = load_knowledge_base()

    assert len(documents) == 23


def test_documents_have_required_metadata():
    documents = load_knowledge_base()

    for document in documents:
        metadata = document.metadata

        assert metadata["document_id"]
        assert metadata["document_type"]
        assert metadata["service"]
        assert metadata["source"]
        assert metadata["status"]

def test_payment_incident_exists():
    documents = load_knowledge_base()

    payment_incident = next(
        document
        for document in documents
        if document.metadata["document_id"] == "INC-1024"
    )

    assert (
        "retry configuration"
        in payment_incident.page_content.lower()
    )

    assert (
        payment_incident.metadata["document_type"]
        == "incident"
    )

    assert (
        payment_incident.metadata["service"]
        == "payment-service"
    )