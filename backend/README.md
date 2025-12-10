# RAG Chatbot Backend

This is the FastAPI backend for the RAG chatbot. It handles data ingestion, embedding generation, Qdrant search, LLM integration, conversational memory, and API security.

## Setup

1.  **Create a virtual environment and install dependencies:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ```

2.  **Set up environment variables:**
    Create a `.env` file in the `backend` directory with the following content:
    ```
    OPENAI_API_KEY=your_openai_api_key
    QDRANT_URL=your_qdrant_cloud_url
    QDRANT_API_KEY=your_qdrant_api_key
    API_KEY=your_backend_api_key
    REDIS_URL=redis://localhost:6379 # Or your Redis instance URL
    ```

3.  **Run the ingestion script:**
    This script will process the book's content, generate embeddings, and upload them to Qdrant.
    ```bash
    python3 scripts/ingest.py
    ```

4.  **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The backend will be running at `http://127.0.0.1:8000`.

## API Endpoints

-   **POST /api/chat**: Handles chat queries and selected text questions.
    -   **Request Body**:
        ```json
        {
            "session_id": "string", (optional)
            "query": "string",
            "selected_text": "string" (optional)
        }
        ```
    -   **Response Body**:
        ```json
        {
            "session_id": "string",
            "response": "string",
            "sources": ["string"]
        }
        ```
    -   **Headers**: `X-API-Key: your_backend_api_key`

## Testing

Run tests using `pytest`:
```bash
pytest
```
