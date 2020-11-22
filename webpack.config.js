const { resolve } = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtract = require("mini-css-extract-plugin");

module.exports = {
  entry: {
    fatpercentage: resolve(__dirname, './concentric/static/js/pages/fatpercentage.js'),
    main: resolve(__dirname, './concentric/static/sass/main.scss'),
  },
  output: {
    filename: '[name].[contenthash].chunk.js',
    // path: resolve(__dirname, './concentric/static/dist/')
    path: resolve(__dirname, './concentric/static/webpack_bundles/')
  },
  optimization: {
    noEmitOnErrors: true,
    splitChunks: {
      chunks: "all",
      name: "common"
    }
  },
  plugins: [
      new BundleTracker({filename: './webpack-stats.json'}),
      new MiniCssExtract({
        filename: "[name].[contenthash].min.css"
      })
  ],
  module: {
    rules: [
      {
        test: /\.css/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.js?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        options: {
          presets: ['@babel/env']
        }
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtract.loader,
          {
            loader: 'css-loader',
            options: {
              url: false
            }
          },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: () => [require('autoprefixer'), require('cssnano')]
              }
            }
          },
          'sass-loader'
        ]
      }
    ]
  },
  resolve: {
      extensions: ['.js']
  }
}
