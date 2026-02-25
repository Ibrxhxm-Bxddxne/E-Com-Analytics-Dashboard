<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useAuthStore } from './stores/auth';

const auth = useAuthStore();
const router = useRouter();

const handleLogout = () => {
  auth.logout();
  router.push('/'); // Redirige vers le login après déconnexion
};
</script>

<template>
  <div id="app-container">
    <nav v-if="auth.token" class="navbar">
      <div class="nav-brand">
        <span class="logo">📊 E-Com Analytics</span>
      </div>
      <div class="nav-links">
        <router-link to="/dashboard" class="nav-item">Dashboard</router-link>
        <button @click="handleLogout" class="btn-logout">Déconnexion</button>
      </div>
    </nav>

    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<style>
/* Styles globaux pour l'application */
:root {
  --primary-color: #42b883;
  --secondary-color: #35495e;
  --bg-color: #f8fafc;
  --text-color: #1e293b;
}

body {
  margin: 0;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background-color: var(--bg-color);
  color: var(--text-color);
}

#app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  z-index: 100;
}

.logo {
  font-weight: bold;
  font-size: 1.2rem;
  color: var(--primary-color);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 20px;
}

.nav-item {
  text-decoration: none;
  color: var(--secondary-color);
  font-weight: 500;
}

.nav-item.router-link-active {
  color: var(--primary-color);
  border-bottom: 2px solid var(--primary-color);
}

.btn-logout {
  background: #fee2e2;
  color: #ef4444;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: background 0.2s;
}

.btn-logout:hover {
  background: #fecaca;
}

.main-content {
  flex: 1;
}
</style>