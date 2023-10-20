const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: (config) => {
    config.module
      .rule('bootstrap-icons')
      .test(/bootstrap-icons\.svg$/)
      .use('html-loader')
      .loader('html-loader')
      .end();
  },
})
