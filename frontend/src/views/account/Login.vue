
<template>
    <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-purple-500 to-pink-500">
      <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <h2 class="text-3xl font-bold text-center text-gray-800 mb-8">Login</h2>
        <form @submit.prevent="handleLogin" class="space-y-6">
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700">Username</label>
            <input
              type="text"
              id="email"
              v-model="form.username"
              placeholder="Enter your email"
              class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-purple-500 focus:border-purple-500"
              required
            />
          </div>
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
            <input
              type="password"
              id="password"
              v-model="form.password"
              placeholder="Enter your password"
              class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-purple-500 focus:border-purple-500"
              required
            />
          </div>
          <div>
            <button
              type="submit"
              class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-purple-600 hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
            >
              Sign In
            </button>
          </div>
        </form>
        <div class="mt-6 text-center">
          <p class="text-sm text-gray-600">
            Don't have an account?
            <router-link :to="{name:'Signup'}" class="font-medium text-purple-600 hover:text-purple-500">Sign up</router-link>
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import api from '@/api';
  export default {
    data() {
      return {
        form: {
          username: '',
          password: '',
        },
      };
    },
    methods: {
            async handleLogin() {
            try {
                const response = await api.post("auth/jwt/create/", this.form);

                localStorage.setItem('access_token', response.data.access);
                localStorage.setItem('refresh_token', response.data.refresh);

                this.$router.push({ name: 'Home'});

            } catch (error) {
                console.error('Login failed:', error.response ? error.response.data : error.message);

                if (error.response) {
                    alert(`Login failed: ${error.response.data.detail || 'Invalid credentials'}`);
                } else {
                    alert('Login failed: Network error or server is down.');
                }
            }
        },
},
  };
  </script>
  
  <style scoped>
  /* Add custom styles here if needed */
  </style>