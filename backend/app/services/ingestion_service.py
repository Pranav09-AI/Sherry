from uuid import uuid4
import uuid
import os

from app.services.document_loader import load_path
from app.services.text_splitter import split_documents
from app.services.embedding import embeddings
from app.services.vector_store import vector_store

def ingest_document(file_path):
    documents = load_path(file_path)


    chunks = split_documents(documents)

    document_id = str(uuid.uuid4())

    source = os.path.basename(file_path)

    for chunk in chunks:
        chunk.metadata["document_id"] = document_id
        chunk.metadata["source"] = source

    uuids = [str(uuid4()) for _ in range(len(chunks))]

    vector_store.add_documents( 
        documents=chunks,
        ids = uuids

    )

    return vector_store

