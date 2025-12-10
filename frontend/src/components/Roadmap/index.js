import React from 'react';
import styles from './styles.module.css';
import useBaseUrl from '@docusaurus/useBaseUrl';

const chapters = [
  { title: 'Introduction', description: 'The big picture of Physical AI.', link: '/docs/chapters/01-introduction' },
  { title: 'Physical AI', description: 'Core concepts and principles.', link: '/docs/chapters/02-physical-ai' },
  { title: 'ROS 2', description: 'The Robot Operating System.', link: '/docs/chapters/03-ros-2' },
  { title: 'Gazebo', description: 'Simulate robots in complex environments.', link: '/docs/chapters/04-gazebo' },
  { title: 'Unity', description: 'Game engine for robotics simulation.', link: '/docs/chapters/05-unity' },
  { title: 'NVIDIA Isaac', description: 'The NVIDIA robotics platform.', link: '/docs/chapters/06-nvidia-isaac' },
  { title: 'VLA', description: 'Vision-Language-Action models.', link: '/docs/chapters/07-vla' },
  { title: 'Humanoids', description: 'The ultimate robotics challenge.', link: '/docs/chapters/08-humanoids' },
  { title: 'Capstone Project', description: 'Build your own humanoid robot.', link: '/docs/chapters/09-capstone' },
  { title: 'Hardware', description: 'The physical components of a robot.', link: '/docs/chapters/10-hardware' },
  { title: 'Cloud Lab', description: 'Cloud-based robotics development.', link: '/docs/chapters/11-cloud-lab' },
  { title: 'Jetson Kit', description: 'Embedded AI at the edge.', link: '/docs/chapters/12-jetson-kit' },
];

export function Roadmap() {
  const baseUrl = useBaseUrl('/');
  return (
    <div className={styles.roadmapContainer}>
      <h2 className={styles.roadmapTitle}>Learning Roadmap</h2>
      <div className={styles.roadmap}>
        {chapters.map((chapter, index) => (
          <div key={index} className={styles.chapter}>
            <div className={styles.chapterNumber}>{index + 1}</div>
            <div className={styles.chapterDetails}>
              <h3 className={styles.chapterTitle}>{chapter.title}</h3>
              <p className={styles.chapterDescription}>{chapter.description}</p>
              <a href={baseUrl + chapter.link.substring(1)} className={styles.chapterLink}>
                Read Chapter
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
