<template>
    <div class="bg-gray-50 dark:bg-gray-900 min-h-screen">
  
      <!-- محتوى المقالة -->
      <div class="container mx-auto px-4 py-8">
        <!-- حالة التحميل -->
        <div v-if="loading" class="text-center">
          <p class="text-gray-600 dark:text-gray-300">Loading article...</p>
        </div>
  
        <!-- حالة الخطأ -->
        <div v-if="error" class="text-center text-red-500">
          <p>Failed to load article. Please try again later.</p>
        </div>
  
        <!-- عرض المقالة -->
        <div v-if="article" class="max-w-4xl mx-auto">
          <!-- صورة المقالة -->
          <img
            :src="article.image"
            :alt="article.title"
            class="w-full h-96 object-cover rounded-lg shadow-lg"
          />
  
          <!-- عنوان المقالة -->
          <h1 class="text-4xl font-bold mt-8 mb-4 text-gray-900 dark:text-white">
            {{ article.title }}
          </h1>
  
          <!-- وصف المقالة -->
          <p class="text-xl text-gray-600 dark:text-gray-300 mb-8">
            {{ article.description }}
          </p>
  
          <!-- محتوى المقالة -->
          <div class="prose prose-lg dark:prose-invert max-w-none" v-html="article.content"></div>
  
          <!-- معلومات المقالة -->
          <div class="mt-8 flex items-center justify-between text-gray-500 dark:text-gray-400">
            <div class="flex items-center">
              <!-- صورة الكاتب -->
              <img
                :src="article.authorImage"
                :alt="article.author"
                class="w-10 h-10 rounded-full mr-2"
              />
              <span>{{ article.author }}</span>
            </div>
            <div class="flex items-center space-x-4">
              <span class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 mr-1"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M2 12h4m14 0h4M12 2v4m0 14v4"
                  />
                </svg>
                <span>{{ article.views }} views</span>
              </span>
              <span class="flex items-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 mr-1"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                  />
                </svg>
                <span>{{ article.likes_count }} likes</span>
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import api from "@/api";
  export default {
    props:['articleId'],
    data() {
      return {
        article: null, // بيانات المقالة
        loading: true, // حالة التحميل
        error: false, // حالة الخطأ
      };
    },
    async mounted() {
      try {
        const response = await api.get(`app/article/${this.articleId}/`);
        this.article = response.data;
      } catch (err) {
        console.error("Failed to fetch article:", err);
        this.error = true;
      } finally {
        this.loading = false;
      }
    },
  };
  </script>
  
  <style>
  /* تخصيصات إضافية */
  .prose {
    color: inherit;
  }
  
  .dark .prose {
    color: #dbd9d9; /* لون النص في وضع الدارك مود */
  }
  </style>