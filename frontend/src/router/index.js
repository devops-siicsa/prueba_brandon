import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
    {
        path: '/',
        redirect: '/dashboard'
    },
    {
        path: '/auth',
        component: () => import('@/layouts/AuthLayout.vue'),
        children: [
            {
                path: 'login',
                name: 'Login',
                component: () => import('@/views/Auth/Login.vue')
            }
        ]
    },
    {
        path: '/',
        component: () => import('@/layouts/MainLayout.vue'),
        meta: { requiresAuth: true },
        children: [
            {
                path: 'dashboard',
                name: 'Dashboard',
                component: () => import('@/views/General/UnderConstruction.vue')
            },
            {
                path: 'config/system',
                name: 'SystemConfig',
                component: () => import('@/views/Config/SystemConfig.vue'),
                meta: { requiresPermission: 'menu:view_sys_config' }
            },
            {
                path: 'config/client',
                name: 'ClientConfig',
                component: () => import('@/views/Config/ClientConfig.vue'),
                meta: { requiresPermission: 'menu:view_client_config' }
            },
            {
                path: 'inventory',
                name: 'InventoryHome',
                component: () => import('@/views/Dashboard/DashboardHome.vue')
            },
            {
                path: 'inventory/list',
                name: 'InventoryList',
                component: () => import('@/views/Inventory/InventoryView.vue')
            },
            {
                path: 'inventory/equipment/:id',
                name: 'EquipmentDetail',
                component: () => import('@/views/Inventory/EquipmentDetail.vue')
            }
        ]
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
})

// Guard de navegación
router.beforeEach(async (to, from, next) => {
    const authStore = useAuthStore()
    const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
    const requiredPermission = to.matched.some(record => record.meta.requiresPermission) ? to.meta.requiresPermission : null

    if (requiresAuth && !authStore.isAuthenticated) {
        // Intentar restaurar sesión
        const restored = await authStore.checkAuth()
        if (!restored) {
            next('/auth/login')
        } else {
            // Sesión restaurada, verificar permisos si aplica
            if (requiredPermission && !authStore.hasPermission(requiredPermission)) {
                next('/dashboard')
            } else {
                next()
            }
        }
    } else if (requiresAuth && requiredPermission && !authStore.hasPermission(requiredPermission)) {
        next('/dashboard')
    } else {
        next()
    }
})

export default router