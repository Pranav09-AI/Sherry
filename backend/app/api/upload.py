from fastapi import APIRouter, UploadFile, File, HTTPException
import os

router = APIRouter()

MAX_FILE_SIZE = 20 * 1024 * 1024


@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Maximum file size is 20 MB."
        )

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as f:
        f.write(content)

    return {
        "filename": file.filename,
        "message": "PDF uploaded successfully."
    }