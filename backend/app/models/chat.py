from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    query: str
    selected_text: Optional[str] = None

class ChatResponse(BaseModel):
    session_id: str
    response: str
    sources: List[str] = []
