from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .llm.release_chain import chain

from backend.app.api.routes.releases import router as releases_router


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)

app.include_router(releases_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReleaseSummaryRequest(BaseModel):
    release_description: str


class ReleaseSummaryResponse(BaseModel):
    release_summary: str


@app.get("/")
def root():
    return {
        "message": "ReleaseLens AI API is running"
    }

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