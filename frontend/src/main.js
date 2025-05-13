import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Naive UI 컴포넌트 수동 등록
import {
  NInput,
  NButton,
  NCard,
  NMessageProvider
} from 'naive-ui'

const app = createApp(App)

app.use(router)

// Naive UI 컴포넌트 글로벌 등록
app.component('n-input', NInput)
app.component('n-button', NButton)
app.component('n-card', NCard)
app.component('n-message-provider', NMessageProvider)

app.mount('#app')
