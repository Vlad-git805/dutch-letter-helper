from pydantic import BaseModel


class LetterAnalyzeRequest(BaseModel):
    text: str
    tone: str = "polite"


class LetterAnalyzeResponse(BaseModel):
    analysis: str