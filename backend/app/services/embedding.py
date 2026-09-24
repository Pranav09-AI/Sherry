from app.config import settings
from langchain_mistralai import MistralAIEmbeddings


embeddings = MistralAIEmbeddings(
    model="mistral-embed",
    api_key=settings.MISTRAL_API_KEY
)


def embed(chunks):
    texts = [chunk.page_content for chunk in chunks]

    vectors = embeddings.embed_documents(texts)

    return vectors

