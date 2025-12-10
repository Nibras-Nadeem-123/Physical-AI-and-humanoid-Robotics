# Deployment Guide for RAG Chatbot

This guide provides instructions for deploying the Integrated RAG Chatbot to production.

## 1. Backend Deployment

### Prerequisites

- Docker or a Python-compatible environment
- Configured environment variables (see `.env.example`)
- A running Qdrant instance (Cloud or self-hosted)
- A Redis instance for rate limiting and session management

### Steps

1.  **Build Docker Image (if using Docker):**
    ```bash
    cd backend
    docker build -t rag-chatbot-backend .
    ```

2.  **Run Docker Container:**
    ```bash
    docker run -d --name rag-chatbot-backend \
      -p 8000:8000 \
      -e OPENAI_API_KEY="your_openai_api_key" \
      -e QDRANT_URL="your_qdrant_url" \
      -e QDRANT_API_KEY="your_qdrant_api_key" \
      -e API_KEY="your_backend_api_key" \
      -e REDIS_URL="your_redis_url" \
      rag-chatbot-backend
    ```

3.  **Manual Deployment (if not using Docker):**
    -   Ensure Python environment is set up.
    -   Install dependencies (`pip install -r requirements.txt`).
    -   Run Uvicorn: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Important Considerations

-   Use a process manager (e.g., Gunicorn, Supervisord, Systemd) for production.
-   Configure a reverse proxy (e.g., Nginx, Caddy) for SSL termination and static file serving.
-   Ensure `OPENAI_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY`, `API_KEY`, and `REDIS_URL` are securely managed (e.g., Kubernetes Secrets, AWS Secrets Manager).

## 2. Frontend Deployment

The frontend is a Docusaurus application. Refer to the official Docusaurus deployment guide for detailed instructions on deploying to various platforms (Netlify, Vercel, GitHub Pages, etc.).

### Prerequisites

-   Built Docusaurus site
-   Configured `REACT_APP_BACKEND_URL` and `REACT_APP_API_KEY` environment variables.

### Steps (Example for Netlify)

1.  **Build the Docusaurus site:**
    ```bash
    cd frontend
    npm run build
    ```

2.  **Deploy `frontend/build` directory:**
    -   Connect your repository to Netlify.
    -   Set `Build command` to `npm run build`.
    -   Set `Publish directory` to `build`.
    -   Configure environment variables (`REACT_APP_BACKEND_URL`, `REACT_APP_API_KEY`) in Netlify.

## 3. Qdrant Ingestion

Ensure the `ingest.py` script is run on the production data to populate the Qdrant collection before the backend service is fully operational.

```bash
cd backend
source .venv/bin/activate
python3 scripts/ingest.py
```

It's recommended to run this as part of your CI/CD pipeline or as a scheduled job for content updates.
