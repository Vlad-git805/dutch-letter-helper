from typing import Literal

from pydantic import BaseModel, Field, field_validator


ReplyTone = Literal["polite", "formal", "friendly", "short"]


class LetterAnalyzeRequest(BaseModel):
    text: str = Field(
        min_length=10,
        max_length=10_000,
        description="Dutch letter, email, or official message to analyze",
    )
    tone: ReplyTone = "polite"

    @field_validator("text", mode="before")
    @classmethod
    def clean_text(cls, value: str) -> str:
        if isinstance(value, str):
            return value.strip()
        return value



class LetterAnalyzeResponse(BaseModel):
    analysis: str