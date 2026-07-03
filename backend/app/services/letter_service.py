from app.ai.client import AIClient
from app.ai.prompts import DUTCH_LETTER_ANALYSIS_PROMPT
from app.schemas.letter import LetterAnalyzeResponse


class LetterService:
    def __init__(self):
        self.ai_client = AIClient()

    def analyze(self, text: str, tone: str = "polite") -> LetterAnalyzeResponse:
        user_message = f"""
            Letter text:
            {text}

            Preferred reply tone:
            {tone}
            """

        ai_response = self.ai_client.generate_response(
            system_prompt=DUTCH_LETTER_ANALYSIS_PROMPT,
            user_message=user_message
        )

        return LetterAnalyzeResponse(
            analysis=ai_response
        )