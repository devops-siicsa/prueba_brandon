import { computed } from 'vue'
import { useAuthStore } from '@/stores/auth'

export function useMenu() {
    const authStore = useAuthStore()

    const menuItems = [
        {
            title: 'Inicio',
            icon: 'mdi-home-outline',
            to: '/dashboard',
            value: 'dashboard'
        },
        {
            title: 'Inventario',
            icon: 'mdi-clipboard-list-outline',
            to: '/inventory',
            value: 'inventory'
        },
        {
            title: 'Panel de Control',
            icon: 'mdi-cog-outline',
            group: 'panel_control',
            children: [
                {
                    title: 'Config. Sistema',
                    icon: 'mdi-tune',
                    to: '/config/system',
                    value: 'sys_config',
                    permission: 'menu:view_sys_config'
                },
                {
                    title: 'Config. Cliente',
                    icon: 'mdi-account-cog-outline',
                    to: '/config/client',
                    value: 'client_config',
                    permission: 'menu:view_client_config'
                }
            ]
        }
    ]

    function filterChildren(children) {
        return children.filter(child => {
            if (!child.permission) return true
            return authStore.hasPermission(child.permission)
        })
    }

    return {
        menuItems,
        filterChildren
    }
}
