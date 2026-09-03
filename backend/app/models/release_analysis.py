from typing import Literal

from pydantic import BaseModel, Field

from backend.app.models.evidence import EvidenceItem


class ReleaseAnalysis(BaseModel):

    risk_level: Literal[
        "low",
        "medium",
        "high",
        "critical",
        "unknown",
    ]

    summary: str

    affected_components: list[str] = Field(
        default_factory=list
    )

    historical_incidents: list[str] = Field(
        default_factory=list
    )

    architecture_decisions: list[str] = Field(
        default_factory=list
    )

    risks: list[str] = Field(
        default_factory=list
    )

    testing_recommendations: list[str] = Field(
        default_factory=list
    )

    evidence: list[EvidenceItem] = Field(
        default_factory=list
    )

    confidence: Literal[
        "low",
        "medium",
        "high",
    ]

    uncertainty: list[str] = Field(
        default_factory=list
    )