# Quickstart: Integrated RAG Chatbot

This guide provides the steps to get the RAG chatbot running locally.

## Prerequisites

- Python 3.11+
- Node.js 20.x+
- Docker
- An OpenAI API key
- A Qdrant Cloud account

## 1. Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the `backend` directory with the following content:
    ```
    OPENAI_API_KEY=your_openai_api_key
    QDRANT_URL=your_qdrant_cloud_url
    QDRANT_API_KEY=your_qdrant_api_key
    ```

4.  **Run the ingestion script:**
    This script will process the book's content, generate embeddings, and upload them to Qdrant.
    ```bash
    python scripts/ingest.py
    ```

5.  **Start the FastAPI server:**
    ```bash
    uvicorn app.main:app --reload
    ```
    The backend will be running at `http://127.0.0.1:8000`.

## 2. Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Start the Docusaurus development server:**
    ```bash
    npm start
    ```
    The frontend will be running at `http://localhost:3000`. The chatbot will be available as a floating button in the bottom-right corner.

## 3. Usage

- Open `http://localhost:3000` in your browser.
- Click the chatbot button to open the chat window.
- Ask questions about the book's content.
- Highlight text on any page and an "Explain" button will appear. Click it to ask the chatbot about the selected text.
