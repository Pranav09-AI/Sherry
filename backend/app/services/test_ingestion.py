from app.services.ingestion_service import ingest_document

ingest_document("uploads/test.pdf")

print("Ingestion successful!")