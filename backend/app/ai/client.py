class AIClient:
    def generate_response(self, system_prompt: str, user_message: str) -> str:
        return (
            "AI Client mock response.\n\n"
            f"System prompt received: {system_prompt[:80]}...\n\n"
            f"User message received: {user_message}"
        )