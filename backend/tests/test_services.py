import pytest
from unittest.mock import MagicMock, patch
from backend.app.services.rag_pipeline import RAGPipeline

@pytest.fixture
def mock_openai_client():
    with patch('backend.app.services.rag_pipeline.client_openai') as mock:
        yield mock

@pytest.fixture
def mock_qdrant_client():
    with patch('backend.app.services.rag_pipeline.client_qdrant') as mock:
        yield mock

@pytest.fixture
def rag_pipeline():
    return RAGPipeline()

def test_generate_embedding(rag_pipeline, mock_openai_client):
    mock_openai_client.embeddings.create.return_value = MagicMock(
        data=[MagicMock(embedding=[0.1, 0.2, 0.3])]
    )
    embedding = rag_pipeline.generate_embedding("test query")
    assert embedding == [0.1, 0.2, 0.3]
    mock_openai_client.embeddings.create.assert_called_once_with(
        input=["test query"],
        model="text-embedding-ada-002"
    )

def test_search_qdrant_for_context(rag_pipeline, mock_qdrant_client):
    mock_qdrant_client.search.return_value = [
        MagicMock(payload={'text': 'context 1'}),
        MagicMock(payload={'text': 'context 2'})
    ]
    context = rag_pipeline.search_qdrant_for_context([0.1, 0.2, 0.3])
    assert context == ['context 1', 'context 2']
    mock_qdrant_client.search.assert_called_once()

def test_generate_answer_with_llm(rag_pipeline, mock_openai_client):
    mock_openai_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="LLM Answer"))]
    )
    answer = rag_pipeline.generate_answer_with_llm("query", ["context"])
    assert answer == "LLM Answer"
    mock_openai_client.chat.completions.create.assert_called_once()

def test_rag_pipeline_run(rag_pipeline, mock_openai_client, mock_qdrant_client):
    mock_openai_client.embeddings.create.return_value = MagicMock(
        data=[MagicMock(embedding=[0.1, 0.2, 0.3])]
    )
    mock_qdrant_client.search.return_value = [
        MagicMock(payload={'text': 'context 1'}),
        MagicMock(payload={'text': 'context 2'})
    ]
    mock_openai_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="Final Answer"))]
    )

    answer, sources = rag_pipeline.run("test query")
    assert answer == "Final Answer"
    assert sources == ['context 1...', 'context 2...']
    mock_openai_client.embeddings.create.assert_called_once()
    mock_qdrant_client.search.assert_called_once()
    mock_openai_client.chat.completions.create.assert_called_once()
