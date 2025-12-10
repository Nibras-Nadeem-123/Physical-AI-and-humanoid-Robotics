import React from 'react';
import styles from './styles.module.css'; // Assuming you'll create a CSS module

function FloatingButton({ onClick }) {
  return (
    <button className={styles.floatingButton} onClick={onClick}>
      💬
    </button>
  );
}

export default FloatingButton;
