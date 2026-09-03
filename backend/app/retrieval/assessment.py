from dataclasses import dataclass

from backend.app.retrieval.models import RetrievedDocument


@dataclass
class RetrievalAssessment:
    documents: list[RetrievedDocument]
    sufficient_evidence: bool
    reason: str


def assess_retrieval(
    documents: list[RetrievedDocument],
    minimum_score: float = 0.75,
    minimum_documents: int = 1,
) -> RetrievalAssessment:

    strong_documents = [
        item
        for item in documents
        if item.score >= minimum_score
    ]

    if len(strong_documents) < minimum_documents:

        return RetrievalAssessment(
            documents=strong_documents,
            sufficient_evidence=False,
            reason=(
                "No sufficiently relevant engineering "
                "evidence was retrieved."
            ),
        )

    return RetrievalAssessment(
        documents=strong_documents,
        sufficient_evidence=True,
        reason="Sufficient relevant evidence was retrieved.",
    )