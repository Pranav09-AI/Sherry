from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.api.upload import router as upload_router

app = FastAPI(
    title="Sherry AI Assistant",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to Vercel URL after deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(upload_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Sherry AI Assistant!",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }