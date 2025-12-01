import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null,
        token: localStorage.getItem('token') || null,
        isAuthenticated: false,
        permissions: [] // Array de códigos de permiso
    }),

    getters: {
        userName: (state) => state.user ? `${state.user.Nombre} ${state.user.Apellido}` : '',
        userRole: (state) => state.user?.Rol || 'Sin Rol',
        hasPermission: (state) => (code) => {
            if (!state.user) return false
            // Super Admin suele tener todo, pero validemos por lista explícita del backend
            return state.permissions.includes(code)
        }
    },

    actions: {
        async login(credentials) {
            try {
                // Conexión real con backend
                // Axios debe estar configurado con withCredentials: true para enviar/recibir cookies
                const response = await axios.post('/api/auth/login', credentials, {
                    withCredentials: true
                })

                if (response.data.requires_2fa) {
                    return { requires_2fa: true, temp_token: response.data.temp_token }
                }

                this.user = response.data.user
                this.permissions = response.data.user.Permisos || []
                this.isAuthenticated = true

                // Fix: Save token for components that need it (like AuditLogList)
                if (response.data.token) {
                    this.token = response.data.token
                    localStorage.setItem('token', response.data.token)
                }

                return { success: true }
            } catch (error) {
                console.error('Login error:', error)
                throw error
            }
        },

        logout() {
            this.user = null
            this.token = null
            this.isAuthenticated = false
            localStorage.removeItem('token')
            // Llamar al backend para limpiar cookie
            axios.post('/api/auth/logout', {}, { withCredentials: true })
        },

        async checkAuth() {
            if (this.isAuthenticated) return true
            try {
                const response = await axios.get('/api/auth/me', { withCredentials: true })
                this.user = response.data
                this.permissions = response.data.Permisos || []
                this.isAuthenticated = true
                return true
            } catch (error) {
                this.user = null
                this.isAuthenticated = false
                this.permissions = []
                return false
            }
        }
    }
})
