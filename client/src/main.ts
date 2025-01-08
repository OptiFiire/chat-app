import { createApp } from 'vue'
import '@/assets/index.css'
import App from '@/App.vue'
import router from './router'
import axios from '@/plugins/axios'
import AccountDropdown from '@/components/AccountDropdown.vue'

const customComponents = [
    AccountDropdown
]

const app = createApp(App)
app.use(router)
app.use(axios)

router.isReady().then(() => {
    app.mount('#app')
})

customComponents.forEach(component => app.component(component.name as string, component))