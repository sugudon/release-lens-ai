from pydantic import BaseModel, Field


class RerankItem(BaseModel):
    document_id: str
    chunk_id: str
    relevance_score: float = Field(
        ge=0.0,
        le=1.0,
    )


class RerankResult(BaseModel):
    results: list[RerankItem]