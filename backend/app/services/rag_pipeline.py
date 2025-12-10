import os
from openai import OpenAI, APIError
from qdrant_client import QdrantClient, models
from qdrant_client.http.exceptions import UnexpectedResponse
from typing import List
from tenacity import retry, wait_random_exponential, stop_after_attempt, RetriableError

# Initialize OpenAI client
client_openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize Qdrant client
QDRANT_URL = os.environ.get("QDRANT_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
client_qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

COLLECTION_NAME = "book_chunks"
EMBEDDING_SIZE = 1536 # For "text-embedding-ada-002"

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6), reraise=True)
def generate_embedding(text: str) -> List[float]:
    """
    Generates an embedding for a given text using OpenAI API with retry logic.
    """
    try:
        response = client_openai.embeddings.create(
            input=[text],
            model="text-embedding-ada-002"
        )
        return response.data[0].embedding
    except APIError as e:
        # Catch OpenAI API errors and re-raise as RetriableError for tenacity
        raise RetriableError(f"OpenAI API error: {e}") from e

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6), reraise=True)
def search_qdrant_for_context(query_embedding: List[float], top_k: int = 5) -> List[str]:
    """
    Searches the Qdrant collection for similar chunks and returns their content with retry logic.
    """
    try:
        search_result = client_qdrant.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=top_k
        )
        context = [hit.payload['text'] for hit in search_result if 'text' in hit.payload]
        return context
    except UnexpectedResponse as e:
        # Catch Qdrant client errors and re-raise as RetriableError for tenacity
        raise RetriableError(f"Qdrant client error: {e}") from e

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6), reraise=True)
def generate_answer_with_llm(query: str, context: List[str], conversation_history: List[dict] = None) -> str:
    """
    Generates an answer using an LLM (OpenAI) based on the query and retrieved context with retry logic.
    """
    messages = [{"role": "system", "content": "You are a helpful assistant that answers questions based on the provided book content."}]

    if conversation_history:
        for turn in conversation_history:
            messages.append({"role": "user", "content": turn["user_query"]})
            messages.append({"role": "assistant", "content": turn["chatbot_response"]})

    context_str = "\n\n".join(context)
    messages.append({"role": "user", "content": f"Based on the following context:\n\n{context_str}\n\nAnswer the question: {query}"})

    try:
        response = client_openai.chat.completions.create(
            model="gpt-3.5-turbo", # Or gpt-4 if preferred
            messages=messages
        )
        return response.choices[0].message.content
    except APIError as e:
        # Catch OpenAI API errors and re-raise as RetriableError for tenacity
        raise RetriableError(f"OpenAI API error: {e}") from e

class RAGPipeline:
    def __init__(self):
        pass

    def run(self, query: str, conversation_history: List[dict] = None) -> (str, List[str]):
        """
        Runs the RAG pipeline to get an answer and relevant sources.
        """
        query_embedding = generate_embedding(query)
        context = search_qdrant_for_context(query_embedding)
        answer = generate_answer_with_llm(query, context, conversation_history)
        sources = [ctx[:100] + "..." for ctx in context] # Simple source representation
        return answer, sources