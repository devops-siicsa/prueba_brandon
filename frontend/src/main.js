import { createApp } from 'vue'
import App from './App.vue'
import { registerSW } from 'virtual:pwa-register'

// Plugins
import { createPinia } from 'pinia'
import router from './router'
import vuetify from './plugins/vuetify'

import permission from './directives/permission'

const updateSW = registerSW({
    onNeedRefresh() {
        // Show a prompt to user to refresh
        console.log('New content available, click on reload button to update.')
    },
    onOfflineReady() {
        console.log('App ready to work offline')
    },
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(vuetify)
app.directive('permission', permission)

app.mount('#app')