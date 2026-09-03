from backend.app.retrieval.factory import (
    create_retriever,
)


def test_payment_query_retrieves_payment_evidence():

    question = (
        "What could be affected by "
        "changing payment retry behavior?"
    )

    retriever = create_retriever(
        top_k=5,
    )

    documents = retriever.invoke(
        question
    )

    assert len(documents) > 0

    document_ids = {
        document.metadata["document_id"]
        for document in documents
    }

    assert (
        "INC-1024" in document_ids
        or "ADR-003" in document_ids
    )