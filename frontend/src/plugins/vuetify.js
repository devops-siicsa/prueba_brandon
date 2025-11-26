// Estilos
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

// Configuración del tema
export default createVuetify({
    theme: {
        defaultTheme: 'light',
        themes: {
            light: {
                colors: {
                    primary: '#223551', // Azul corporativo SIICSA
                    secondary: '#616367', // Gris corporativo
                    accent: '#00A08F', // Verde corporativo
                    error: '#FF5252',
                    info: '#2196F3',
                    success: '#4CAF50',
                    warning: '#FFC107',
                    background: '#FFFFFF', // Blanco fondo
                },
            },
        },
    },
})