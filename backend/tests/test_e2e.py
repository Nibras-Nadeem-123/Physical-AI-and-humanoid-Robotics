import os
import pytest
import httpx
from fastapi.testclient import TestClient
from backend.app.main import app # Import your FastAPI app

# Use TestClient for in-process testing
client = TestClient(app)

@pytest.fixture
def api_key():
    return os.environ.get("API_KEY", "your_default_api_key")

def test_e2e_normal_chat_flow(api_key):
    """
    Tests the full end-to-end flow for a normal chat query.
    This test assumes the backend is running and Qdrant is populated.
    """
    headers = {"X-API-Key": api_key}
    session_id = "e2e_test_session_normal"
    
    # 1. Initial query
    payload1 = {
        "session_id": session_id,
        "query": "What is the role of ROS 2 in robotics?",
        "selected_text": None
    }
    
    with httpx.Client() as client: # Use httpx.Client for real network requests
        response1 = client.post("http://localhost:8000/api/chat", json=payload1, headers=headers)
    
    assert response1.status_code == 200
    response_data1 = response1.json()
    assert response_data1["session_id"] == session_id
    assert "ROS 2" in response_data1["response"] # A plausible check
    assert len(response_data1["sources"]) > 0
    print(f"Initial Response: {response_data1['response']}")

    # 2. Follow-up query to test memory
    payload2 = {
        "session_id": session_id,
        "query": "How does it differ from its predecessor?",
        "selected_text": None
    }

    with httpx.Client() as client:
        response2 = client.post("http://localhost:8000/api/chat", json=payload2, headers=headers)

    assert response2.status_code == 200
    response_data2 = response2.json()
    assert response_data2["session_id"] == session_id
    assert "ROS 1" in response_data2["response"] or "DDS" in response_data2["response"] # Plausible checks
    print(f"Follow-up Response: {response_data2['response']}")

def test_e2e_selected_text_flow(api_key):
    """
    Tests the end-to-end flow for a query with selected text.
    """
    headers = {"X-API-Key": api_key}
    session_id = "e2e_test_session_selected_text"
    
    selected_text = "NVIDIA Isaac Sim is a powerful robotics simulation platform that allows for the development, testing, and training of AI-based robots in a photorealistic, physically-accurate virtual environment."
    query = "Explain this in simpler terms."
    
    payload = {
        "session_id": session_id,
        "query": query,
        "selected_text": selected_text
    }
    
    with httpx.Client() as client:
        response = client.post("http://localhost:8000/api/chat", json=payload, headers=headers)

    assert response.status_code == 200
    response_data = response.json()
    assert response_data["session_id"] == session_id
    assert "virtual environment" in response_data["response"] or "simulation" in response_data["response"]
    print(f"Selected Text Response: {response_data['response']}")

def test_e2e_invalid_api_key():
    """
    Tests that the API correctly rejects a request with an invalid API key.
    """
    headers = {"X-API-Key": "invalid_key_12345"}
    payload = {
        "session_id": "test_invalid_key",
        "query": "Does this work?",
        "selected_text": None
    }
    
    with httpx.Client() as client:
        response = client.post("http://localhost:8000/api/chat", json=payload, headers=headers)

    assert response.status_code == 403 # Forbidden
    assert "Could not validate credentials" in response.text

if __name__ == "__main__":
    pytest.main([__file__])