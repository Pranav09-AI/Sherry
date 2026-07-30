from google import genai 
from app.config import settings 

class GeminiService:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate_response(self, prompt: str) -> str:
        response = self.client.interactions.create(
            model = "gemini-3.6-flash",
            input = prompt,
        )

        return response.output_text

gemini_service = GeminiService()