import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapeVue from 'bootstrap-vue'


import './assets/main.css'

Vue.use(BootstrapeVue);
const app = createApp(App)

app.use(router)

app.mount('#app')
