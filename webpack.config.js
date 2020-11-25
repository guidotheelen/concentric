const { resolve } = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

const isDevelopment = process.env.NODE_ENV === 'development'

module.exports = {
  mode: isDevelopment? "development" : "production",
  entry: {
    fatpercentage: resolve(__dirname, './concentric/static/js/pages/fatpercentage.js'),
    main: resolve(__dirname, './concentric/static/sass/main.scss'),
  },
  output: {
    filename: '[name].[contenthash].chunk.js',
    path: resolve(__dirname, './concentric/static/dist/')
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
      new MiniCssExtractPlugin({
        filename: isDevelopment ? '[name].css' : '[name].[hash].css',
        chunkFilename: isDevelopment ? '[id].css' : '[id].[hash].css'
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
        test: /\.module\.s(a|c)ss$/,
        loader: [
          isDevelopment ? 'style-loader' : MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              modules: true,
              sourceMap: isDevelopment
            }
          },
          {
            loader: 'sass-loader',
            options: {
              sourceMap: isDevelopment
            }
          }
        ]
      },
      {
         test: /\.s(a|c)ss$/,
         exclude: /\.module.(s(a|c)ss)$/,
         loader: [
           isDevelopment ? 'style-loader' : MiniCssExtractPlugin.loader,
           'css-loader',
           {
             loader: 'sass-loader',
             options: {
               sourceMap: isDevelopment
             }
           }
         ]
       }
    ]
  },
  resolve: {
      extensions: ['.js', '.scss']
  }
}
