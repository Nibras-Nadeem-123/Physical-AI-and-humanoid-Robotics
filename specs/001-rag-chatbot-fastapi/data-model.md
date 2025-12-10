# Data Model: Integrated RAG Chatbot

This document defines the data structures used in the RAG chatbot application.

## 1. Backend: Python (FastAPI)

### ChatRequest
Represents an incoming chat query from the frontend.

- `session_id: str` (Optional): A unique identifier for the conversation session. If not provided, a new session is created.
- `query: str`: The user's question.
- `selected_text: str` (Optional): The text highlighted by the user.

### ChatResponse
Represents the chatbot's response to the frontend.

- `session_id: str`: A unique identifier for the conversation session.
- `response: str`: The chatbot's answer.
- `sources: List[str]`: A list of sources from the book that were used to generate the answer (e.g., chapter titles or section numbers).

### ConversationTurn
A single turn in a conversation.

- `user_query: str`: The user's query for this turn.
- `chatbot_response: str`: The chatbot's response for this turn.

### Session
Represents a single conversation.

- `session_id: str`: A unique identifier for the conversation.
- `history: List[ConversationTurn]`: A list of the last 5 conversation turns.

## 2. Vector Database (Qdrant)

### BookChunk
Represents a chunk of text from the book stored in Qdrant.

- `vector: List[float]`: The embedding vector for the text chunk.
- `payload: Dict`:
  - `text: str`: The raw text of the chunk.
  - `source: str`: The source of the text (e.g., "Chapter 1: Introduction").
  - `page_number: int`: The page number where the text can be found.

## 3. Frontend: React

### ChatMessage
Represents a single message in the chat window.

- `id: str`: A unique identifier for the message.
- `text: str`: The content of the message.
- `sender: 'user' | 'bot'`: Who sent the message.
- `sources: List[str]` (Optional): For bot messages, a list of sources.
