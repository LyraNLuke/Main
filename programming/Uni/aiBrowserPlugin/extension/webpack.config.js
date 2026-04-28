const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = [
  {
    name: 'popup',
    entry: './src/popup/index.tsx',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'popup.js',
    },
    module: {
      rules: [
        {
          test: /\.tsx?$/,
          use: 'ts-loader',
          exclude: /node_modules/,
        },
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
        },
      ],
    },
    resolve: {
      extensions: ['.tsx', '.ts', '.js'],
    },
    plugins: [
      new CopyPlugin({
        patterns: [
          { from: 'manifest.json', to: '.' },
          { from: 'public', to: '.' },
        ],
      }),
    ],
  },
  {
    name: 'background',
    entry: './src/background/service-worker.ts',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'background.js',
    },
    module: {
      rules: [
        {
          test: /\.tsx?$/,
          use: 'ts-loader',
          exclude: /node_modules/,
        },
      ],
    },
    resolve: {
      extensions: ['.tsx', '.ts', '.js'],
    },
  },
  {
    name: 'content',
    entry: './src/content/content.ts',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'content.js',
    },
    module: {
      rules: [
        {
          test: /\.tsx?$/,
          use: 'ts-loader',
          exclude: /node_modules/,
        },
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],
        },
      ],
    },
    resolve: {
      extensions: ['.tsx', '.ts', '.js'],
    },
  },
];
