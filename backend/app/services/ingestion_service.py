import uuid 
import os

from app.services.document_loader import load_path
from app.services.text_splitter import split_documents
from app.services.embedding import embeddings
from app.services.vector_store import create_vector_store

def ingest_document(file_path):
    documents = load_path(file_path)

    chunks = split_documents(documents)
    print("Number of chunks:", len(chunks))

    document_id = str(uuid.uuid4())

    source = os.path.basename(file_path)

    vector_store = create_vector_store(
        chunks,
        document_id,
        source,
        embeddings
    )

    return vector_store

