<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-8 text-gray-900 dark:text-white">Articles</h1>

    <!-- Loading State -->
    <div v-if="loading" class="text-center">
      <p class="text-gray-600 dark:text-gray-300">Loading articles...</p>
    </div>

    <!-- Error State -->
    <div v-if="error" class="text-center text-red-500">
      <p>Failed to load articles. Please try again later.</p>
    </div>

    <!-- Articles Display -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <router-link
        v-for="article in articles"
        :key="article.id"
        :to="{ name: 'ArticlePage', params: { articleId: article.id }}"
        
        class="bg-white dark:bg-gray-800 shadow-lg rounded-lg overflow-hidden transition-all duration-300 hover:shadow-xl"
      >
        <!-- Article Image -->
        <img
          :src="article.image"
          class="w-full h-48 object-cover"
          alt="Article Image"
        />

        <div class="p-6">
          <!-- Article Category -->
          <span
            class="inline-block bg-blue-100 text-blue-800 text-sm font-semibold px-2 py-1 rounded-full mb-2 dark:bg-blue-200 dark:text-blue-900"
          >
            {{ article.category }}
          </span>

          <!-- Article Title -->
          <h2 class="text-xl font-semibold mb-2 text-gray-900 dark:text-white">
            {{ article.title }}
          </h2>

          <!-- Article Description -->
          <p class="text-gray-600 dark:text-gray-300 mb-4">
            {{ article.description }}
          </p>

          <!-- Article Info (Author and Views) -->
          <div class="flex items-center justify-between text-gray-500 dark:text-gray-400">
            <div class="flex items-center">
              <!-- Author Image -->
              <img
                :src="article.authorImage"
                class="w-8 h-8 rounded-full mr-2"
              />
              <span>{{ article.author }}</span>
            </div>
            <div class="flex items-center">
              <span>{{ article.views }} views</span>
            </div>
          </div>

          <!-- Like Button and Count -->
          <div class="mt-4 flex items-center">
            <span
              class="flex items-center text-gray-500 dark:text-gray-400 hover:text-red-500 transition-colors duration-200"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 mr-1"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                />
              </svg>
              <span>{{ article.likes_count }}</span>
            </span>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>


<script>
import api from "@/api";

export default {
  data() {
    return {
      articles: [], // سيتم ملء هذا المصفوفة بالبيانات من API
      loading: true, // حالة التحميل
      error: false, // حالة الخطأ
    };
  },
  async mounted() {
    try {
      // جلب البيانات من API
      const response = await api.get("app/article/"); // استبدل برابط API الفعلي
      this.articles = response.data; // تعيين البيانات المستردة إلى المصفوفة
    } catch (err) {
      console.error("Failed to fetch articles:", err);
      this.error = true; // عرض رسالة الخطأ
    } finally {
      this.loading = false; // إيقاف حالة التحميل
    }
  },
};
</script>

<style scoped>
/* يمكنك إضافة تخصيصات إضافية هنا */
</style>