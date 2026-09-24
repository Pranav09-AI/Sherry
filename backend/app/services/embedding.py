from app.config import settings
from langchain_mistralai import MistralAIEmbeddings


embeddings = MistralAIEmbeddings(
    model="mistral-embed",
    api_key=settings.MISTRAL_API_KEY
)


