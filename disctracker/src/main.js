import './assets/main.css'

// main.js (or where your Vue app is initialized)

import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import Dashboard from './views/dashboard.vue'; // Import your existing home page component
import Loginview from './views/loginview.vue'; // Import your existing home page component
//import About from './views/About.vue'; // Import your new page component

const routes = [
    { path: '/', component: Loginview},
    { path: '/dashboard', component: Dashboard },
//  { path: '/about', component: About }, // Define a route for your new page
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);
app.use(router);
app.mount('#app');
