from typing import List, Dict, Optional
from backend.app.models.memory import Session, ConversationTurn
from backend.app.services.rag_pipeline import RAGPipeline

class ChatService:
    def __init__(self):
        self.sessions: Dict[str, Session] = {}
        self.rag_pipeline = RAGPipeline()

    def _get_session(self, session_id: str) -> Session:
        if session_id not in self.sessions:
            self.sessions[session_id] = Session(session_id=session_id)
        return self.sessions[session_id]

    def process_chat_query(self, session_id: str, query: str, selected_text: Optional[str] = None) -> (str, List[str]):
        session = self._get_session(session_id)
        
        # Prepare conversation history for RAG pipeline
        history_for_rag = [{"user_query": turn.user_query, "chatbot_response": turn.chatbot_response} 
                           for turn in session.history]

        full_query = f"{selected_text}\n{query}" if selected_text else query
        
        answer, sources = self.rag_pipeline.run(full_query, history_for_rag)

        # Update session history (keep last 5 turns)
        session.history.append(ConversationTurn(user_query=query, chatbot_response=answer))
        if len(session.history) > 5:
            session.history = session.history[-5:]

        return answer, sources
