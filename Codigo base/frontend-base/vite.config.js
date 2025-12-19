import { fileURLToPath, URL } from 'node:url' 
import { defineConfig } from 'vite' 
import vue from '@vitejs/plugin-vue' 
import vueDevTools from 'vite-plugin-vue-devtools' 
import vuetify from 'vite-plugin-vuetify'; 

// https://vite.dev/config/ 
export default defineConfig({ 
  plugins: [ 
    vue(), 
    vueDevTools(), 
    vuetify(), 
  ], 
  resolve: { 
    alias: { 
      '@': fileURLToPath(new URL('./src', import.meta.url)) 
    }, 
  },
  base: '/', // Asegura rutas limpias en producción
  build: {
    outDir: 'dist', // Asegura que el build vaya a frontend/dist
    emptyOutDir: true
  },
})
