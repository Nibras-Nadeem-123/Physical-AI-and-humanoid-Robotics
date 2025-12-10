import React, { useState, useEffect } from 'react';
import { useLocation } from '@docusaurus/router';
import FloatingButton from '../../components/Chatbot/FloatingButton';
import ChatWindow from '../../components/Chatbot/ChatWindow';
import useTextSelection from '../../hooks/useTextSelection'; // Import the new hook

function Root({ children }) {
  const [isChatOpen, setIsChatOpen] = useState(false);
  const location = useLocation();
  const selectedText = useTextSelection(); // Use the new hook

  const isChatVisible = !location.pathname.startsWith('/blog') && !location.pathname.startsWith('/docs');

  const toggleChat = () => {
    setIsChatOpen((prev) => !prev);
  };

  useEffect(() => {
    // Optionally open chat window if text is selected, or just make it available
    if (selectedText && !isChatOpen) {
      // You might want to automatically open the chat here or show a prompt
      // For now, we'll just ensure the selected text is captured.
      console.log("Text selected:", selectedText);
    }
  }, [selectedText, isChatOpen]);

  return (
    <>
      {children}
      {isChatVisible && (
        <>
          <FloatingButton onClick={toggleChat} />
          {isChatOpen && <ChatWindow onClose={toggleChat} selectedText={selectedText} />}
        </>
      )}
    </>
  );
}

export default Root;