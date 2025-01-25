<template>
  <!-- Main Content -->
  <div class="container mx-auto px-6 py-8 dark:bg-gray-900">
    <!-- Create New Article Card -->
    <p class="text-gray-600 dark:text-gray-400 text-center mt-2">If you nead to update an article, just enter to create and put the title article you want to update</p>
    <router-link
      :to="{ name: 'CreateArticle' }"
      class="block bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md hover:scale-105 transition-transform duration-300 mb-8"
    >
      <div class="flex items-center justify-center space-x-4">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-12 w-12 text-blue-600 dark:text-blue-400"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 6v6m0 0v6m0-6h6m-6 0H6"
          />
        </svg>
        <h2 class="text-xl font-bold text-gray-800 dark:text-gray-200">
          Create New Article
        </h2>
      </div>
      <p class="text-gray-600 dark:text-gray-400 text-center mt-2">
        Start a new article and share your knowledge with the world.
      </p>
      
    </router-link>

    <!-- Statistics -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200">
          Number of Articles
        </h2>
        <p class="text-3xl font-bold text-blue-600 dark:text-blue-400 mt-2" v-text="articles.length"></p>
      </div>

      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200">
          Total Revenue
        </h2>
        <p class="text-3xl font-bold text-green-600 dark:text-green-400 mt-2">SAR {{ totalRevenue }}</p>
      </div>

      <div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200">
          Number of Followers
        </h2>
        <p class="text-3xl font-bold text-purple-600 dark:text-purple-400 mt-2">
          {{ followersCount }}
        </p>
      </div>
    </div>

    <!-- Article List -->
    <div class="mt-8">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-gray-200 mb-6">
        My Articles
      </h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="article in articles"
          :key="article.id"
          class="bg-white dark:bg-gray-800 rounded-lg shadow-md overflow-hidden hover:scale-105 transition-transform duration-300"
        >
          <router-link
            :to="{ name: 'ArticlePage', params: { articleId: article.id }}"
            class="block"
          >
            <img
              loading="lazy"
              :src="article.image || 'https://via.placeholder.com/300'"
              :alt="article.title"
              class="w-full h-48 object-cover"
            />
            <div class="p-6">
              <h3 class="text-xl font-bold text-gray-800 dark:text-gray-200 mb-2">
                {{ article.title }}
              </h3>
              <p class="text-gray-600 dark:text-gray-400 text-sm mb-4">
                {{ article.introduction }}
              </p>
              <div class="flex justify-between items-center">
                <span class="text-sm text-gray-600 dark:text-gray-400">
                  {{ formatDate(article.created_at) }}
                </span>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/api';

export default {
  data() {
    return {
      articles: [],
      totalRevenue: 0,
      followersCount: 0,
    };
  },
  async mounted() {
    try {
      // جلب البيانات من الـ API
      const response = await api('app/user/');
      const data = response.data;

      // تعيين البيانات المسترجعة
      this.articles = data.articles;
      this.totalRevenue = data.totalRevenue || 0; // إذا لم يكن هناك إيرادات، نعيينها إلى 0
      this.followersCount = data.followers.length || 0; // إذا لم يكن هناك متابعين، نعيينها إلى 0
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString();
    },
  },
};
</script>