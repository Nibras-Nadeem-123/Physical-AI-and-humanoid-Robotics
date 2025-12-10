import React, { useState, useEffect } from 'react';
import styles from './styles.module.css';
import { sendMessage } from '../../../services/api'; // Import the API service

function ChatWindow({ onClose, selectedText }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [sessionId, setSessionId] = useState(null); // Manage session ID

  useEffect(() => {
    if (selectedText) {
      setInput(selectedText);
    }
  }, [selectedText]);

  const handleSendMessage = async () => {
    if (input.trim()) {
      const userMessage = { text: input, sender: 'user' };
      setMessages((prevMessages) => [...prevMessages, userMessage]);
      setInput('');

      try {
        const response = await sendMessage(sessionId, input, selectedText);
        setSessionId(response.session_id); // Update session ID from backend
        const botMessage = { text: response.response, sender: 'bot', sources: response.sources };
        setMessages((prevMessages) => [...prevMessages, botMessage]);
      } catch (error) {
        console.error('Error sending message:', error);
        const errorMessage = { text: 'Sorry, something went wrong. Please try again.', sender: 'bot' };
        setMessages((prevMessages) => [...prevMessages, errorMessage]);
      }
    }
  };

  return (
    <div className={styles.chatWindow}>
      <div className={styles.chatHeader}>
        <h3>Chatbot</h3>
        <button onClick={onClose}>X</button>
      </div>
      <div className={styles.chatBody}>
        {messages.map((msg, index) => (
          <div key={index} className={`${styles.chatMessage} ${styles[msg.sender]}`}>
            {msg.text}
            {msg.sources && msg.sources.length > 0 && (
              <div className={styles.chatSources}>
                (Sources: {msg.sources.join(', ')})
              </div>
            )}
          </div>
        ))}
      </div>
      <div className={styles.chatInput}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
          placeholder={selectedText ? `Ask about "${selectedText.substring(0, 20)}..."` : "Ask me anything..."}
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
}

export default ChatWindow;
