# Research: Integrated RAG Chatbot

This document addresses key questions and decisions for the RAG chatbot implementation.

## 1. Persistent Storage for Conversational History

**Decision**: Use Redis for session storage.
**Rationale**: While in-memory storage is simple, it does not scale beyond a single backend instance and is not persistent. Redis provides a fast, scalable, and persistent solution for managing conversational history, which is crucial for the target of 100+ concurrent users and for providing a seamless user experience across multiple sessions or backend restarts.
**Alternatives considered**:
- **In-memory dictionary**: Simple but not scalable or persistent.
- **Database (e.g., PostgreSQL)**: More complex to set up and slower than Redis for this use case.

## 2. Handling Queries Outside Book Scope

**Decision**: When the RAG pipeline fails to find relevant context in the book, the chatbot will respond with a predefined, helpful message.
**Rationale**: The feature spec requires that the chatbot's answers be derived only from the book's content. Providing a "I don't know" type of response is honest and prevents hallucination. The message should guide the user to rephrase their question or search for a different topic. Example response: "I'm sorry, but I couldn't find a relevant answer in the book for your question. Please try rephrasing it or asking about a different topic."
**Alternatives considered**:
- **Allowing LLM to answer without context**: This would violate FR-005 and could lead to inaccurate or fabricated answers.
- **No response**: Poor user experience.

## 3. Docusaurus Integration Strategy

**Decision**: Use Docusaurus's "swizzling" feature to wrap the root layout with a custom component that includes the chatbot.
**Rationale**: Swizzling is the recommended way to add custom components and logic to the global layout of a Docusaurus site. This approach ensures that the chatbot's floating button is present on all pages and that the modal can be displayed as an overlay. It is cleaner than manually injecting scripts or using post-build modifications.
**Alternatives considered**:
- **Manual script injection**: More brittle and could break with Docusaurus updates.
- **Theme component shadowing**: Shadowing is better for replacing specific components, whereas swizzling is more suited for wrapping the entire layout.

## 4. Choice of OpenAI SDK

**Decision**: Use the standard OpenAI Python SDK for interacting with the API.
**Rationale**: The user mentioned "OpenAI Agents or ChatKit SDK". The standard OpenAI Python SDK is sufficient for the answer generation part of the RAG pipeline. It is well-documented, stable, and directly supported by OpenAI. "Agents" are a higher-level concept and might introduce unnecessary complexity. "ChatKit" seems to be a third-party library, and it's better to stick with the official SDK.
**Alternatives considered**:
- **OpenAI Agents**: More complex than needed for this project.
- **ChatKit SDK**: A third-party library which is not needed.
- **LangChain's OpenAI integration**: This will be used, but it's a wrapper around the OpenAI Python SDK.
