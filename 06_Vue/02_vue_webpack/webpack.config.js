const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')

module.exports = {
  mode: 'development',
  // 여러개의 js 파일의 시작점 ( 웹팩이 파일을 읽기 시작하는 지점)
  entry: {
    app: path.join(__dirname, 'src', 'main.js')
  },
  // 웹팩은 js만 변환이 가능하기 때문에 CSS, HTML 같은 모듈을 통해서 웹패이 이해할 수 있는것으로 변화 ㄴ
  module: {
    rules:[
      {
        test: /\.vue$/,
        use: 'vue-loader',
      },
      {
        test: /\.css$/,
        use: ['vue-style-loader','css-loader'],
      },
    ]
  },
  // 웹팩을 통해서 번들된 결과물을 추가적으로 처리하는 부분 (옵션)
  plugins: [
    new VueLoaderPlugin(),
  ],
  // 여러 개의 js 파일을 하나로 만들어낸 결과물.
  output: {
    filename: 'app.js',
    path: path.join(__dirname, 'dist')
  },
}