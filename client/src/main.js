import './assets/index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './misc/router'
import components from './misc/components'

const app = createApp(App)
app.use(createPinia())
app.use(components)
app.use(router)

router.isReady().then(() => app.mount('#app'))
