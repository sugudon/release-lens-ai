from pydantic import BaseModel, Field


class ReleaseAnalysisRequest(BaseModel):
    release_description: str = Field(
        ...,
        min_length=10,
        description="Description of the proposed software release",
    )