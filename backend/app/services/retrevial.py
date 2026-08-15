from langchain_chroma import Chroma
from app.services.embedding import embeddings

vector_store = Chroma(
    collection_name="sherry_documents",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)

def retrieve(query: str)-> str:
    result = vector_store.similarity_search (
        query = query,
        k = 3
    )

    for doc in result:
        print(doc.page_content)

    return result


