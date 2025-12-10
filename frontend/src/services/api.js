const API_BASE_URL = process.env.NODE_ENV === 'production'
  ? 'https://your-production-backend-url.com/api' // TODO: Replace with actual production URL
  : 'http://localhost:8000/api';

const API_KEY = process.env.REACT_APP_API_KEY || 'your_default_api_key'; // TODO: Use a secure way to handle API keys

export async function sendMessage(sessionId, query, selectedText = null) {
  try {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': API_KEY,
      },
      body: JSON.stringify({ session_id: sessionId, query, selected_text: selectedText }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || 'Failed to send message');
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('API call error:', error);
    throw error;
  }
}
