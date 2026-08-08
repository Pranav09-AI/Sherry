from langchain_google_genai import GoogleGenerativeAIEmbeddings


def embed(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        output_dimensionality=768
    )

    vectors = embeddings.embed_documents(chunks)

    return vectors