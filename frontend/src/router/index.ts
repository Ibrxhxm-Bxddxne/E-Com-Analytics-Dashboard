import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Dashboard from '../views/Dashboard.vue'; // À créer ensuite

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Login },
    { 
      path: '/dashboard', 
      component: Dashboard,
      beforeEnter: (to, from, next) => {
        // Protection de la route
        if (!localStorage.getItem('token')) next('/')
        else next()
      }
    }
  ]
});

export default router;