import { useAuthStore } from '@/stores/auth'

export default {
    mounted(el, binding) {
        const { value } = binding
        const authStore = useAuthStore()

        if (value && value instanceof String || typeof value === 'string') {
            const hasPermission = authStore.hasPermission(value)

            if (!hasPermission) {
                el.parentNode && el.parentNode.removeChild(el)
            }
        } else {
            throw new Error(`Necesitas especificar el permiso, ej: v-permission="'auth:login'"`)
        }
    }
}
