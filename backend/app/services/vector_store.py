import uuid

from langchain_chroma import Chroma


def create_vector_store(chunks, document_id, source, embeddings):

    ids = []

    for chunk in chunks:
        chunk.metadata["document_id"] = document_id
        chunk.metadata["source"] = source

        ids.append(str(uuid.uuid4()))

    vector_store = Chroma(
        collection_name="sherry_documents",
        embedding_function=embeddings,
        persist_directory="./chroma_db",
    )

    vector_store.add_documents(
        documents=chunks,
        ids=ids
    )

    return vector_store