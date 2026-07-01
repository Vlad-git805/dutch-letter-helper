from pydantic import BaseModel


class LetterAnalyzeRequest(BaseModel):
    text: str
    tone: str = "polite"