from backend.app.models.evidence import EvidenceItem


def validate_citations(
    evidence: list[EvidenceItem],
    retrieved_document_ids: set[str],
) -> list[EvidenceItem]:

    valid_evidence = []

    for item in evidence:

        if item.document_id in retrieved_document_ids:
            valid_evidence.append(item)

    return valid_evidence