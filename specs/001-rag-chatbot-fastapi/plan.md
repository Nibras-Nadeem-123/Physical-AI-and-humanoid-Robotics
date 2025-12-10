# Implementation Plan: Integrated RAG Chatbot

**Branch**: `001-rag-chatbot-fastapi` | **Date**: 2025-12-09 | **Spec**: [./spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-rag-chatbot-fastapi/spec.md`

## Summary

This plan outlines the architecture and implementation strategy for an integrated Retrieval-Augmented Generation (RAG) chatbot. The system will feature a FastAPI backend for processing queries and managing conversational memory, a Qdrant vector database for efficient content retrieval from the textbook, and a React-based frontend embedded within the Docusaurus site. The chatbot will answer user questions based on the book's content, either from a general query or user-selected text, while maintaining a 5-turn conversational history.

## Technical Context

**Language/Version**: Python 3.11, Node.js 20.x
**Primary Dependencies**:
- **Backend**: FastAPI, Uvicorn, LangChain, OpenAI Python SDK, Qdrant Client
- **Frontend**: React 18, Docusaurus, CSS-in-JS (e.g., Styled Components)
- **Vector Database**: Qdrant Cloud (Free Tier)
**Storage**: In-memory session storage for conversational history (NEEDS CLARIFICATION: For scalability, should we consider a persistent store like Redis?)
**Testing**: Pytest (backend), Jest/React Testing Library (frontend)
**Target Platform**: Web (Docusaurus)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: p95 response latency < 3 seconds
**Constraints**: Must operate within Qdrant Cloud Free Tier limits. OpenAI API usage and costs must be monitored.
**Scale/Scope**: Target of 100+ concurrent users.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Notes |
|---|---|---|
| **Code Quality & Formatting** | PASS | Adherence to PEP 8 (Python) and community React standards will be enforced via linting. |
| **Testing Principles** | PASS | Unit and integration tests will be required for both backend and frontend components to ensure verifiability and accuracy. |
| **Performance Considerations** | PASS | Performance goals are explicitly defined (p95 < 3s). Caching strategies for embeddings and API responses may be explored. |
| **Security Guidelines** | PASS | API keys will be managed via environment variables. Rate limiting will be implemented. Input sanitization will be performed to prevent injection attacks. |
| **Architecture & Design** | PASS | The proposed architecture is modular (backend, frontend, DB) and follows standard web application patterns. |
| **Content Style & Tone** | N/A | Not directly applicable to the chatbot implementation, but the chatbot's personality should align with the book's tone. |
| **Safety & Ethics Rules** | PASS | The chatbot will be designed to only use book content, preventing harmful or off-topic responses. A guardrail will be implemented to handle queries outside the book's scope gracefully. |

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-chatbot-fastapi/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── openapi.yml
└── tasks.md             # Phase 2 output (NOT created by this command)
```

### Source Code (repository root)

```text
backend/
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   └── chat.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── services/
│   │   ├── chat_service.py
│   │   └── rag_pipeline.py
│   ├── models/
│   │   ├── chat.py
│   │   └── memory.py
│   └── main.py
├── tests/
│   ├── test_api.py
│   └── test_services.py
└── scripts/
    └── ingest.py

frontend/
├── src/
│   ├── components/
│   │   ├── Chatbot/
│   │   │   ├── ChatWindow.js
│   │   │   ├── FloatingButton.js
│   │   │   └── index.js
│   │   └── __tests__/
│   ├── services/
│   │   └── api.js
│   └── theme/
│       └── Root.js # Docusaurus swizzled component for global layout
└── tests/
    └── setup.js
```

**Structure Decision**: The project is a web application with a distinct frontend and backend, making the "Web application" structure the most appropriate choice. This separation of concerns facilitates independent development, testing, and deployment. The backend will contain the FastAPI application and ingestion scripts, while the frontend will house the React-based chatbot components and Docusaurus integration.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| N/A | N/A | N/A |