from openai import OpenAI, OpenAIError

from app.core.settings import settings

from app.ai.exceptions import AIClientError


class AIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )
    def generate_response(
    self,
    system_prompt: str,
    user_message: str,
    ) -> str:
        try:
            response = self.client.responses.create(
                model=settings.OPENAI_MODEL,
                temperature=settings.OPENAI_TEMPERATURE,
                instructions=system_prompt,
                input=user_message,
            )

            return response.output_text

        except OpenAIError as exc:
            raise AIClientError(
                "Failed to generate an AI response."
            ) from exc