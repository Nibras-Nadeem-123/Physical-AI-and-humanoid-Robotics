# RAG Chatbot Frontend

This is the React-based frontend for the RAG chatbot, integrated into a Docusaurus site. It provides a floating chat button and a modal chat window.

## Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    ```bash
    npm install
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the `frontend` directory with the following content:
    ```
    REACT_APP_API_KEY=your_backend_api_key
    ```
    *(Note: For Docusaurus, you might need to prefix environment variables with `DANGEROUSLY_DISABLE_ESLINT_NO_DEV_ERRORS=true`)*

4.  **Start the Docusaurus development server:**
    ```bash
    npm start
    ```
    The frontend will be running at `http://localhost:3000`. The chatbot will be available as a floating button in the bottom-right corner.

## Linting and Formatting

Run ESLint to check for code quality:
```bash
npx eslint src/
```

Run Prettier to format the code:
```bash
npx prettier --write src/
```
