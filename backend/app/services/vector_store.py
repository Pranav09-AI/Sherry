from langchain_chroma import Chroma

def create_vector_store(chunks, embeddings, source):
    for chunk in chunks:
        chunk.metadata["source"] = source

    vector_store = Chroma(
        collection_name="Sherry_documents",
        embedding_function=embeddings,
        persist_directory="./chroma_db",
    )

    vector_store.add_documents(chunks)

    return vector_store