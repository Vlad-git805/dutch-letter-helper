from openai import OpenAI, OpenAIError

from app.core.settings import settings

from app.ai.exceptions import AIClientError

from app.schemas.letter import LetterAnalyzeResponse


class AIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
    def generate_response(
    self,
    system_prompt: str,
    user_message: str,
    ) -> LetterAnalyzeResponse:
        try:
            response = self.client.responses.parse(
                model=settings.OPENAI_MODEL,
                temperature=settings.OPENAI_TEMPERATURE,
                instructions=system_prompt,
                input=user_message,
                text_format=LetterAnalyzeResponse,
            )

            if response.output_parsed is None:
                raise AIClientError(
                    "AI response could not be parsed."
                )

            return response.output_parsed

        except OpenAIError as exc:
            raise AIClientError(
                "Failed to generate an AI response."
            ) from exc