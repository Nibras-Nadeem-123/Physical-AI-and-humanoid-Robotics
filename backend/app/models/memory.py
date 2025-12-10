from pydantic import BaseModel
from typing import List

class ConversationTurn(BaseModel):
    user_query: str
    chatbot_response: str

class Session(BaseModel):
    session_id: str
    history: List[ConversationTurn] = []
