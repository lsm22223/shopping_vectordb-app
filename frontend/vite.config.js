import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'  //  경로 유틸 추가

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')  // @ → src 디렉토리
    }
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        secure: false,
        ws: true,
        configure: (proxy, options) => {
          proxy.on('error', (err, req, res) => {
            console.log('프록시 에러:', err);
          });
          proxy.on('proxyReq', (proxyReq, req, res) => {
            console.log('프록시 요청:', req.url);
          });
        }
      }
    }
  }
})

