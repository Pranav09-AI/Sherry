from fastapi import APIRouter,UploadFile, File

router = APIRouter()

@router.post("/upload") 

def upload_document(file: UploadFile = File(...)):
    return{
        "filename": file.filename,
        "message": "File received successfully"
    }

