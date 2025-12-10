from fastapi import APIRouter, HTTPException, Depends
from backend.app.models.chat import ChatRequest, ChatResponse
from backend.app.services.chat_service import ChatService
from backend.app.core.security import get_api_key
from fastapi_limiter.depends import RateLimiter

router = APIRouter()
chat_service = ChatService()

@router.post("/chat", response_model=ChatResponse, dependencies=[Depends(RateLimiter(times=5, seconds=10))])
async def chat(request: ChatRequest, api_key: str = Depends(get_api_key)):
    try:
        response, sources = chat_service.process_chat_query(
            session_id=request.session_id,
            query=request.query,
            selected_text=request.selected_text
        )
        return ChatResponse(session_id=request.session_id, response=response, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
