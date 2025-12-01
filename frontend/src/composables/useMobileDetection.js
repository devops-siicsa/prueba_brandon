import { computed } from 'vue'
import { useDisplay } from 'vuetify'

export function useMobileDetection() {
    const { platform } = useDisplay()

    const isMobileApp = computed(() => {
        // --- CAPA 1: Preguntar a Vuetify (Reactive) ---
        if (platform.android || platform.ios) return true

        // --- CAPA 2: Detección Manual (Fallback de Seguridad) ---
        // Si Vuetify tarda en reaccionar, leemos el User Agent directamente.
        // Esto soluciona el error donde platform.android es true pero la computed da false.
        if (typeof navigator !== 'undefined') {
            const ua = navigator.userAgent.toLowerCase()

            // Regex simple para Android y iPhone
            const esAndroidPuro = /android/.test(ua)
            const esIphone = /iphone|ipod/.test(ua)

            if (esAndroidPuro || esIphone) return true

            // --- CAPA 3: El caso del "iPad Mentiroso" ---
            // Si el sistema dice ser Mac/Linux/Win, pero tiene pantalla táctil (dedos)
            const esMacOculto = platform.mac || /macintosh|mac os x/.test(ua)
            const tieneTactil = navigator.maxTouchPoints > 0

            if (esMacOculto && tieneTactil) return true
        }

        return false
    })

    return {
        isMobileApp,
        platform
    }
}