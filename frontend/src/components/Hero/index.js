import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';
import useBaseUrl from '@docusaurus/useBaseUrl';

export function Hero({ children }) {
  return <div className={styles.hero}>{children}</div>;
}

export function HeroBanner({ children }) {
  return <div className={styles.heroBanner}>{children}</div>;
}

export function HeroTitle({ children }) {
  return <h1 className={styles.heroTitle}>{children}</h1>;
}

export function HeroSubtitle({ children }) {
  return <p className={styles.heroSubtitle}>{children}</p>;
}

export function HeroButtons({ children, to }) {
    const baseUrl = useBaseUrl(to);
  return <div className={styles.heroButtons}><a href={baseUrl} className="button button--primary button--lg">{children}</a></div>;
}
