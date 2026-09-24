from langchain_core.documents import Document
from app.services.vector_store import vector_store



def retrieve(query: str)-> list[Document]:
    result = vector_store.similarity_search (
        query = query,
        k = 3
    )

    return result


