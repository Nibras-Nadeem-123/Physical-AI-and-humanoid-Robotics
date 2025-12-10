# Tasks: Integrated RAG Chatbot

**Input**: Design documents from `/specs/001-rag-chatbot-fastapi/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup

**Purpose**: Project initialization and basic structure

- [x] T001 Create backend and frontend directory structures as per `plan.md`.
- [x] T002 [P] Initialize Python project with FastAPI in `backend/`.
- [x] T003 [P] Initialize React project with Docusaurus in `frontend/`.
- [x] T004 [P] Configure linting and formatting for Python (black, ruff) in `backend/`.
- [x] T005 [P] Configure linting and formatting for Javascript (eslint, prettier) in `frontend/`.

---

## Phase 2: Foundational (Data Ingestion & Embeddings)

**Purpose**: Core data pipeline that MUST be complete before ANY user story can be implemented.

- [x] T006 Create script `backend/scripts/ingest.py` for data ingestion.
- [x] T007 In `backend/scripts/ingest.py`, implement logic to extract full book content.
- [x] T008 In `backend/scripts/ingest.py`, implement text cleaning and normalization.
- [x] T009 In `backend/scripts/ingest.py`, implement content chunking.
- [x] T010 In `backend/scripts/ingest.py`, implement embedding generation using OpenAI API.
- [x] T011 [P] In `backend/scripts/ingest.py`, implement Qdrant collection creation.
- [x] T012 In `backend/scripts/ingest.py`, implement vector uploading to Qdrant.
- [x] T013 Create a validation script/test to verify vector search accuracy.

---

## Phase 3: User Story 1 - Query on Book Content (Priority: P1) 🎯 MVP

**Goal**: A reader can ask a question and get an answer from the book.

**Independent Test**: Ask "What is Physical AI?". The chatbot should provide a definition from the book.

### Implementation for User Story 1

- [x] T014 [US1] Create chat models in `backend/app/models/chat.py`.
- [x] T015 [US1] Create memory models in `backend/app/models/memory.py`.
- [x] T016 [US1] Implement RAG pipeline service in `backend/app/services/rag_pipeline.py`.
- [x] T017 [US1] Implement Chat service in `backend/app/services/chat_service.py`.
- [x] T018 [US1] Implement chat endpoint in `backend/app/api/endpoints/chat.py`.
- [x] T019 [P] [US1] Implement API key security in `backend/app/core/security.py`.
- [x] T020 [P] [US1] Implement rate limiting.
- [x] T021 [P] [US1] Create React component `frontend/src/components/Chatbot/FloatingButton.js`.
- [x] T022 [P] [US1] Create React component `frontend/src/components/Chatbot/ChatWindow.js`.
- [x] T023 [US1] Implement API service in `frontend/src/services/api.js` to connect to backend.
- [x] T024 [US1] Integrate chatbot into Docusaurus in `frontend/src/theme/Root.js`.

---

## Phase 4: User Story 2 - Query on Selected Text (Priority: P2)

**Goal**: A reader can highlight text and ask a question about it.

**Independent Test**: Highlight a paragraph, trigger the chatbot, and verify the explanation is relevant.

### Implementation for User Story 2

- [x] T025 [US2] Enhance `backend/app/api/endpoints/chat.py` to handle `selected_text`.
- [x] T026 [US2] Enhance `backend/app/services/rag_pipeline.py` to use selected text as primary context.
- [x] T027 [US2] Implement text selection capture on the frontend.
- [x] T028 [US2] Update `frontend/src/components/Chatbot/ChatWindow.js` to send selected text to the backend.

---

## Phase 5: Testing & Validation

- [x] T029 [P] Unit tests for RAG pipeline in `backend/tests/test_services.py`.
- [x] T030 [P] Unit tests for memory handling in `backend/tests/test_models.py`.
- [x] T031 Integration test for Qdrant retrieval.
- [x] T032 End-to-end test for normal chat flow.
- [ ] T033 End-to-end test for selected-text flow.

---

## Phase 6: Performance & Reliability

- [x] T034 Load testing for 100+ concurrent users.
- [x] T035 Latency benchmarking and optimization.
- [x] T036 Implement retry strategy for OpenAI/Qdrant failures.

---

## Phase 7: Documentation & Delivery

- [x] T037 [P] Create `backend/README.md` with setup instructions.
- [x] T038 [P] Create `frontend/README.md` with setup instructions.
- [x] T039 [P] Create environment configuration guide.
- [x] T040 Write deployment guide.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** must complete before all other phases.
- **Foundational (Phase 2)** must complete before user stories.
- **User Stories (Phase 3 & 4)** can be worked on after Phase 2 is complete.
- **Testing, Performance, and Documentation** can be worked on in parallel with user stories.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. Complete relevant tasks from Phase 5, 6, 7 for US1.
5. **STOP and VALIDATE**: Test User Story 1 independently.
