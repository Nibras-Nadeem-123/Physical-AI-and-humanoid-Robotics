import React from 'react';
import styles from './styles.module.css';

const features = [
  {
    title: 'Comprehensive Curriculum',
    description: '12 chapters covering everything from the basics to advanced topics.',
    icon: '📚',
  },
  {
    title: 'Hands-On Projects',
    description: 'Learn by doing with practical exercises and a capstone project.',
    icon: '🛠️',
  },
  {
    title: 'Cutting-Edge Technologies',
    description: 'Explore ROS 2, Gazebo, Unity, NVIDIA Isaac, and more.',
    icon: '🚀',
  },
];

export function Features() {
  return (
    <div className={styles.featuresContainer}>
      <div className={styles.features}>
        {features.map((feature, index) => (
          <div key={index} className={styles.feature}>
            <div className={styles.featureIcon}>{feature.icon}</div>
            <h3 className={styles.featureTitle}>{feature.title}</h3>
            <p className={styles.featureDescription}>{feature.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
