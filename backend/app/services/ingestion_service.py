import uuid 
import os


from services.document_loader import load_path
from services.text_splitter import split_documents
from services.vector_store import create_vector_store
from services.embedding import embeddings

def ingest_document(file_path):
    documents = load_path(file_path)

    chunks = split_documents(documents)

    document_id = str(uuid.uuid4())

    source = os.path.basename(file_path)

    vector_store = create_vector_store(
        chunks,
        document_id,
        source,
        embeddings
    )

    return vector_store

