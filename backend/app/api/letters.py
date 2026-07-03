from fastapi import APIRouter

from app.schemas.letter import LetterAnalyzeRequest, LetterAnalyzeResponse
from app.services.letter_service import LetterService

router = APIRouter(
    prefix="/letters",
    tags=["letters"]
)

letter_service = LetterService()


@router.post("/analyze", response_model=LetterAnalyzeResponse)
def analyze_letter(request: LetterAnalyzeRequest):
    result = letter_service.analyze(
        text=request.text,
        tone=request.tone
    )

    return result