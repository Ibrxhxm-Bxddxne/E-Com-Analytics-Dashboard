<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const errorMsg = ref('');
const loading = ref(false);

const auth = useAuthStore();
const router = useRouter();

const handleLogin = async () => {
  loading.ref = true;
  errorMsg.value = '';
  
  const success = await auth.login(username.value, password.value);
  
  if (success) {
    router.push('/dashboard'); // Redirection après succès
  } else {
    errorMsg.value = "Identifiants invalides ou serveur hors ligne.";
  }
  loading.value = false;
};
</script>

<template>
  <div class="login-container">
    <div class="login-card">
      <h2>Connexion Dashboard</h2>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label>Utilisateur</label>
          <input v-model="username" type="text" required placeholder="Ex: admin" />
        </div>
        
        <div class="form-group">
          <label>Mot de passe</label>
          <input v-model="password" type="password" required />
        </div>

        <p v-if="errorMsg" class="error">{{ errorMsg }}</p>

        <button type="submit" :disabled="loading">
          {{ loading ? 'Connexion en cours...' : 'Se connecter' }}
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f7fa;
}
.login-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
}
.form-group { margin-bottom: 1rem; }
input { width: 100%; padding: 0.5rem; margin-top: 0.5rem; }
button { width: 100%; padding: 0.7rem; background: #42b883; color: white; border: none; cursor: pointer; }
.error { color: red; font-size: 0.9rem; }
</style>