<template>
  <div
    class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-500 to-indigo-600"
  >
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <h2 class="text-3xl font-bold text-center text-gray-800 mb-8">Sign Up</h2>

      <!-- Success Message -->
      <div
        v-if="successMessage"
        class="mb-4 p-4 text-sm text-green-700 bg-green-100 rounded-lg dark:bg-green-200 dark:text-green-800"
        role="alert"
      >
        {{ successMessage }}
      </div>

      <!-- Error Message -->
      <div
        v-if="errorMessage"
        class="mb-4 p-4 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800"
        role="alert"
      >
        {{ errorMessage }}
      </div>

      <form @submit.prevent="handleSignUp" class="space-y-6">
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700"
            >Username</label
          >
          <input
            type="text"
            id="username"
            v-model="form.username"
            placeholder="Enter your username"
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700"
            >Email</label
          >
          <input
            type="email"
            id="email"
            v-model="form.email"
            placeholder="Enter your email"
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700"
            >Password</label
          >
          <input
            type="password"
            id="password"
            v-model="form.password"
            placeholder="Enter your password"
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div>
          <label
            for="confirmPassword"
            class="block text-sm font-medium text-gray-700"
            >Confirm Password</label
          >
          <input
            type="password"
            id="confirmPassword"
            v-model="form.confirmPassword"
            placeholder="Confirm your password"
            class="mt-1 block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
            required
          />
        </div>
        <div>
          <button
            type="submit"
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            Sign Up
          </button>
        </div>
      </form>
      <div class="mt-6 text-center">
        <p class="text-sm text-gray-600">
          Already have an account?
          <router-link
            :to="{ name: 'Login' }"
            class="font-medium text-blue-600 hover:text-blue-500"
            >Log in</router-link
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/api"; // Import your API configuration.

export default {
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
      },
      successMessage: '',
      errorMessage: '',
    };
  },
  methods: {
    async handleSignUp() {
      try {
        // Reset messages
        this.successMessage = '';
        this.errorMessage = '';

        // Send signup request
        const response = await api.post("auth/users/", this.form);

        // Handle success
        if (response.status === 201) {
          this.successMessage = "Your account has been created successfully!";
          this.form = {
            username: '',
            email: '',
            password: '',
            confirmPassword: '',
          };
          setTimeout(() => {
            this.$router.push({ name: 'Login' });
          }, 2000); // Redirect after 2 seconds
        }
      } catch (error) {
        // Handle errors
        if (error.response) {
          this.errorMessage =
            error.response.data ||
            "There was an error creating your account.";
        } else {
          this.errorMessage = "Network error. Please try again later.";
        }
      }
    },
  },
};
</script>
