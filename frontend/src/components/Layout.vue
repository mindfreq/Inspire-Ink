<template>
  <div class="min-h-screen flex flex-col bg-white dark:bg-gray-900">
    <NavBar />

    <!-- Main Content -->
    <main class="flex-grow container mx-auto p-4">
      <router-view />
    </main>
  </div>
</template>

<script>
import NavBar from './NavBar.vue';
export default {
  name: 'Layout',
  components: {
    NavBar
  }
}
</script>