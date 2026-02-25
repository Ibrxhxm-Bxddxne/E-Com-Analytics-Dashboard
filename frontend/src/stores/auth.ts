import { defineStore } from 'pinia';
import api from '../api';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
  }),
  actions: {
    async login(username: string, password: string) {
      try {
        const response = await api.post('token/', { username, password });
        this.token = response.data.access;
        localStorage.setItem('token', this.token as string);
        return true;
      } catch (error) {
        console.error("Erreur de connexion", error);
        return false;
      }
    },
    logout() {
      this.token = null;
      localStorage.removeItem('token');
    }
  }
});