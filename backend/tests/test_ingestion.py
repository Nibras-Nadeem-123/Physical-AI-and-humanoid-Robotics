import os
import sys
from qdrant_client import QdrantClient
from openai import OpenAI

# Add the ingest script to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from ingest import EMBEDDING_SIZE, COLLECTION_NAME

# Initialize OpenAI client
client_openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize Qdrant client
QDRANT_URL = os.environ.get("QDRANT_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
client_qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

def generate_query_embedding(text):
    """
    Generates an embedding for a given text using OpenAI API.
    """
    response = client_openai.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def search_qdrant(query_text, top_k=3):
    """
    Searches the Qdrant collection for similar chunks.
    """
    query_embedding = generate_query_embedding(query_text)
    search_result = client_qdrant.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=top_k
    )
    return search_result

def main():
    """
    Validation script to test Qdrant vector search accuracy.
    """
    print("Running vector search accuracy validation...")

    # Example queries
    queries = [
        "What is Physical AI?",
        "Explain ROS 2 in brief.",
        "What are humanoid robots?"
    ]

    for query in queries:
        print(f"\nQuery: '{query}'")
        search_results = search_qdrant(query)
        for i, hit in enumerate(search_results):
            print(f"  Result {i+1} (score: {hit.score:.4f}):")
            print(f"    Content: {hit.payload['text'][:200]}...") # Print first 200 chars
            # Add more metadata if available in payload

    print("\nVector search accuracy validation complete.")

if __name__ == "__main__":
    main()
