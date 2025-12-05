import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import vuetify from 'vite-plugin-vuetify'
import { VitePWA } from 'vite-plugin-pwa'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
    // Cargar variables de entorno basadas en el modo (development, production, etc.)
    const env = loadEnv(mode, process.cwd(), '')
    const apiUrl = env.VITE_API_URL || 'http://localhost:5000'

    return {
        plugins: [
            vue(),
            // Vuetify plugin para cargar solo los componentes que usemos (Tree shaking)
            vuetify({ autoImport: true }),
            VitePWA({
                registerType: 'autoUpdate',
                includeAssets: ['favicon.ico', 'apple-touch-icon.png', 'masked-icon.svg'],
                manifest: {
                    name: 'Sistema de Inventario',
                    short_name: 'Inventario',
                    description: 'Sistema de Gestión de Inventario SIICSA',
                    theme_color: '#ffffff',
                    icons: [
                        {
                            src: 'pwa-192x192.png',
                            sizes: '192x192',
                            type: 'image/png'
                        },
                        {
                            src: 'pwa-512x512.png',
                            sizes: '512x512',
                            type: 'image/png'
                        }
                    ]
                },
                workbox: {
                    runtimeCaching: [
                        {
                            // Usar RegExp constructor para crear patrón dinámico
                            urlPattern: new RegExp(`^${apiUrl}/api/config/catalogs/.*$`),
                            handler: 'StaleWhileRevalidate',
                            options: {
                                cacheName: 'api-catalogs-cache',
                                expiration: {
                                    maxEntries: 50,
                                    maxAgeSeconds: 60 * 60 * 24 * 7 // 7 days
                                }
                            }
                        },
                        {
                            urlPattern: new RegExp(`^${apiUrl}/api/inventory/equipos.*$`),
                            handler: 'NetworkFirst',
                            options: {
                                cacheName: 'api-inventory-cache',
                                networkTimeoutSeconds: 10,
                                expiration: {
                                    maxEntries: 100,
                                    maxAgeSeconds: 60 * 60 * 24 // 1 day
                                },
                                cacheableResponse: {
                                    statuses: [0, 200]
                                }
                            }
                        }
                    ]
                }
            })
        ],
        resolve: {
            alias: {
                '@': path.resolve(__dirname, './src'),
            },
        },
        server: {
            port: 3000, // Correremos el frontend en el puerto 3000
            allowedHosts: true, // Permitir acceso desde ngrok u otros hosts externos
            proxy: {
                '/api': {
                    target: apiUrl,
                    changeOrigin: true,
                    secure: false,
                }
            }
        }
    }
})