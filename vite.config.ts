import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/reader/',
  server: {
    proxy: {
      '/api': {
        target: 'https://openapi.youdao.com',
        changeOrigin: true
      }
    }
  },
  resolve: {
    alias: {
      path: 'path-browserify'
    }
  }
})
