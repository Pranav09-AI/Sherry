from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
load_dotenv()


embeddings = MistralAIEmbeddings(
    model="mistral-embed",
)


def embed(chunks):
    texts = [chunk.page_content for chunk in chunks]

    vectors = embeddings.embed_documents(texts)

    return vectors

