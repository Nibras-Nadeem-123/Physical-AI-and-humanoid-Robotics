module.exports = {
  extends: ['eslint:recommended', 'plugin:react/recommended', 'prettier'],
  plugins: ['react'],
  rules: {
    'react/react-in-jsx-scope': 'off',
  },
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module',
    ecmaFeatures: {
      jsx: true,
    },
  },
  env: {
    browser: true,
    node: true,
    es6: true,
  },
  settings: {
    react: {
      version: 'detect',
    },
  },
};
