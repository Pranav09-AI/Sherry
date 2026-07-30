from fastapi import APIRouter 

from app.schemas.chat import ChatRequest, ChatResponse 
from app.services.gemini_service import gemini_service 
from app.services.prompt_service import prompt_service

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    final_prompt = prompt_service.build_prompt(
        request.message
    )

    response = gemini_service.generate_response(
        final_prompt
    )

    return ChatResponse(
        response=response
    )

   