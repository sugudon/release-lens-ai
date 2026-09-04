from fastapi import APIRouter

from backend.app.models.release import ReleaseAnalysisRequest
from backend.app.models.release_analysis import ReleaseAnalysis
from backend.app.services.release_analysis import analyze_release


router = APIRouter(
    prefix="/api/releases",
    tags=["Releases"],
)


@router.post(
    "/analyze",
    response_model=ReleaseAnalysis,
)
def analyze_release_endpoint(
    request: ReleaseAnalysisRequest,
):
    return analyze_release(
        request.release_description
    )