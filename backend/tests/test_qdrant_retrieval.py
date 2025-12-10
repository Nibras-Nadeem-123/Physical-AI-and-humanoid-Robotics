import os
import sys
import pytest
from qdrant_client import QdrantClient
from openai import OpenAI

# Add the ingest script to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from ingest import COLLECTION_NAME

# Initialize OpenAI client
client_openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize Qdrant client
QDRANT_URL = os.environ.get("QDRANT_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")

@pytest.fixture
def qdrant_client():
    if not QDRANT_URL or not QDRANT_API_KEY:
        pytest.skip("QDRANT_URL or QDRANT_API_KEY not set, skipping integration tests.")
    return QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def generate_query_embedding(text):
    """
    Generates an embedding for a given text using OpenAI API.
    """
    response = client_openai.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def test_qdrant_retrieval(qdrant_client):
    """
    Tests that a query to Qdrant returns a plausible result.
    """
    query_text = "What is reinforcement learning?"
    query_embedding = generate_query_embedding(query_text)

    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=3
    )

    assert search_result is not None
    assert len(search_result) > 0
    
    # Check that the payload has the 'text' key
    for hit in search_result:
        assert 'text' in hit.payload
        assert isinstance(hit.payload['text'], str)
        print(f"Retrieved text (score: {hit.score:.4f}): {hit.payload['text'][:100]}...")

if __name__ == "__main__":
    pytest.main([__file__])
