const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'A 12-Chapter Textbook on the Future of Embodied Intelligence',
  favicon: 'img/logo.svg',

  // Set the production url of your site here
  url: 'https://nibras-nadeem-123.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: 'Physical-AI-and-humanoid-Robotics/',

  // GitHub pages deployment config.
  organizationName: 'nibras-nadeem-123',
  projectName: 'Physical-AI-and-humanoid-Robotics',
deploymentBranch: 'gh-pages',
trailingSlash: false,
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn', 

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/ai-driven-development/physical-ai-and-humanoid-robotic-textbook/tree/main/',
        },
        blog: {
          showReadingTime: true,
          editUrl:
            'https://github.com/ai-driven-development/physical-ai-and-humanoid-robotic-textbook/tree/main/',
          blogSidebarCount: 'ALL',
          blogSidebarTitle: 'All Posts',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        respectPrefersColorScheme: true,
      },
      // Replace with your project's social card
      image: 'img/social-card.jpg',
      navbar: {
        title: 'Physical AI & Humanoid Robotics',
        logo: {
          alt: 'Physical AI Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'chapters',
            position: 'left',
            label: 'Textbook',
          },
          {to: 'blog', label: 'Blog', position: 'left'},
          {
            href: 'https://github.com/ai-driven-development/physical-ai-and-humanoid-robotic-textbook',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Learn',
            items: [
              {
                label: 'Textbook',
                to: 'docs/chapters/01-introduction',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Discord',
                href: 'https://discord.gg/invite/docusaurus',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/docusaurus',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Blog',
                to: 'blog',
              },
              {
                label: 'GitHub',
                href: 'https://github.com/ai-driven-development/physical-ai-and-humanoid-robotic-textbook',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} AI Driven Development. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
