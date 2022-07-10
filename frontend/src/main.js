import { createApp } from 'vue'
import App from './App.vue'

import 'mdb-vue-ui-kit/css/mdb.min.css';
import router from './router'
import store from './store'

import axios from 'axios'



//axios.defaults.baseURL = 'https://localhost8080'
axios.defaults.baseURL = 'http://furnitureapp.pl/'



createApp(App).use(store).use(router, axios).mount('#app')