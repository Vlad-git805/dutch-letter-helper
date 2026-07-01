class LetterService:
    def analyze(self, text: str, tone: str = "polite") -> dict:
        return {
            "summary": "This is a test analysis.",
            "detected_tone": tone,
            "original_text": text,
            "message": "LetterService is working!"
        }