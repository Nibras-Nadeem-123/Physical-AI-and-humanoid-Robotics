import pytest
from backend.app.models.memory import ConversationTurn, Session
from backend.app.services.chat_service import ChatService
from unittest.mock import MagicMock, patch

def test_conversation_turn_model():
    turn = ConversationTurn(user_query="Hello", chatbot_response="Hi there!")
    assert turn.user_query == "Hello"
    assert turn.chatbot_response == "Hi there!"

def test_session_model():
    session = Session(session_id="test_session_123")
    assert session.session_id == "test_session_123"
    assert session.history == []

    turn1 = ConversationTurn(user_query="Q1", chatbot_response="A1")
    session.history.append(turn1)
    assert len(session.history) == 1
    assert session.history[0].user_query == "Q1"

@pytest.fixture
def mock_rag_pipeline():
    with patch('backend.app.services.chat_service.RAGPipeline') as MockRAGPipeline:
        instance = MockRAGPipeline.return_value
        instance.run.return_value = "Mocked RAG Answer", ["Source 1"]
        yield instance

def test_chat_service_new_session(mock_rag_pipeline):
    chat_service = ChatService()
    session_id = "new_session"
    query = "What is AI?"
    
    answer, sources = chat_service.process_chat_query(session_id, query)
    
    assert answer == "Mocked RAG Answer"
    assert sources == ["Source 1"]
    assert session_id in chat_service.sessions
    assert len(chat_service.sessions[session_id].history) == 1
    assert chat_service.sessions[session_id].history[0].user_query == query
    assert chat_service.sessions[session_id].history[0].chatbot_response == answer
    mock_rag_pipeline.run.assert_called_once()

def test_chat_service_existing_session_with_history(mock_rag_pipeline):
    chat_service = ChatService()
    session_id = "existing_session"
    
    # Pre-populate history
    chat_service.sessions[session_id] = Session(
        session_id=session_id,
        history=[
            ConversationTurn(user_query="PrevQ1", chatbot_response="PrevA1"),
            ConversationTurn(user_query="PrevQ2", chatbot_response="PrevA2"),
        ]
    )
    
    query = "Tell me more."
    answer, sources = chat_service.process_chat_query(session_id, query)
    
    assert answer == "Mocked RAG Answer"
    assert len(chat_service.sessions[session_id].history) == 3
    assert chat_service.sessions[session_id].history[2].user_query == query
    assert chat_service.sessions[session_id].history[2].chatbot_response == answer
    mock_rag_pipeline.run.assert_called_once()
    args, _ = mock_rag_pipeline.run.call_args
    assert "PrevQ1" in args[1][0]["user_query"] # Check if history passed to RAG

def test_chat_service_history_limit(mock_rag_pipeline):
    chat_service = ChatService()
    session_id = "limited_session"
    
    # Pre-populate history with more than 5 turns
    history_items = [ConversationTurn(user_query=f"Q{i}", chatbot_response=f"A{i}") for i in range(10)]
    chat_service.sessions[session_id] = Session(
        session_id=session_id,
        history=history_items
    )
    
    query = "Last question."
    answer, sources = chat_service.process_chat_query(session_id, query)
    
    assert len(chat_service.sessions[session_id].history) == 5
    assert chat_service.sessions[session_id].history[0].user_query == "Q6" # Ensure oldest was dropped
    assert chat_service.sessions[session_id].history[-1].user_query == query
    mock_rag_pipeline.run.assert_called_once()
    args, _ = mock_rag_pipeline.run.call_args
    assert len(args[1]) == 4 # Ensure only last 4 turns were passed to RAG, plus current query
