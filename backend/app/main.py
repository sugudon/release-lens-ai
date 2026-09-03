from fastapi import FastAPI
from pydantic import BaseModel

from .config import settings
from .llm.release_chain import chain


app = FastAPI(
    title=settings.app_name,
    version="0.2.0",
)


class ReleaseSummaryRequest(BaseModel):
    release_description: str


class ReleaseSummaryResponse(BaseModel):
    release_summary: str


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.app_env,
    }


@app.post(
    "/releases/summarize",
    response_model=ReleaseSummaryResponse,
)
def summarize_release(request: ReleaseSummaryRequest):
    result = chain.invoke(
        {
            "release_description": request.release_description,
        }
    )

    return ReleaseSummaryResponse(
        release_summary=result
    )