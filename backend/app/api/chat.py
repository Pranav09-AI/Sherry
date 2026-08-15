from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.gemini_service import gemini_service
from app.services.prompt_service import prompt_service
from app.services.retrevial import retrieve

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    results = retrieve(request.message) 

    context = ""

    for doc in results:
        context += doc.page_content + "\n\n"

    print(context)


    for doc in results:
        print(doc.page_content)
        print("=" * 50)

    final_prompt = prompt_service.build_prompt(
        request.message,
        context
    )

    response = gemini_service.generate_response(
        final_prompt
    )

    return ChatResponse(
        response=response
    )