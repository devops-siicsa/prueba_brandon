import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import * as labs from 'vuetify/labs/components' // 👈 Importar labs

import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

const vuetify = createVuetify({
  components: {
    ...components,
    ...labs, // 👈 Habilitar todos los labs, incluido VCalendar
  },
  directives,
})

createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app')
