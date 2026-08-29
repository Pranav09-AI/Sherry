from app.services.vector_store import vector_store
from app.services.embedding import embeddings



def retrieve(query: str)-> str:
    result = vector_store.similarity_search (
        query = query,
        k = 3
    )

    for doc in result:
        print(doc.page_content)

    return result


