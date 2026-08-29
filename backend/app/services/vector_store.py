import os
from pinecone import Pinecone
from dotenv import load_dotenv
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from app.services.embedding import embeddings
from app.config import settings 
load_dotenv()

pinecone_api_key = settings.PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)


index_name = "sherry"

if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension=1024,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
index = pc.Index(index_name)

vector_store = PineconeVectorStore(index = index, embedding=embeddings)