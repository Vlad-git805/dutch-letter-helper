from app.ai.client import AIClient
from app.ai.prompts import build_dutch_letter_analysis_prompt
from app.schemas.letter import LetterAnalyzeResponse


class LetterService:
    def __init__(self):
        self.ai_client = AIClient()

    def analyze(
        self,
        text: str,
        tone: str = "polite"
    ) -> LetterAnalyzeResponse:

        system_prompt = build_dutch_letter_analysis_prompt(
            reply_tone=tone
        )

        user_message = f"Letter text:\n\n{text}"

        ai_response = self.ai_client.generate_response(
            system_prompt=system_prompt,
            user_message=user_message
        )

        return LetterAnalyzeResponse(
            analysis=ai_response
        )