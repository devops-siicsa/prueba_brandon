import { createApp } from 'vue'
import App from './App.vue'

// Plugins
import { createPinia } from 'pinia'
import router from './router'
import vuetify from './plugins/vuetify'

import permission from './directives/permission'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(vuetify)
app.directive('permission', permission)

app.mount('#app')