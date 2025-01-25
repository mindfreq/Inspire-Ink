<template>
  <div class="create-article max-w-2xl mx-auto p-6 bg-white dark:bg-gray-800 rounded-lg shadow-md">
    <h1 class="text-2xl font-bold mb-6 text-gray-900 dark:text-white">Create a New Article</h1>
    <form @submit.prevent="saveArticle">
      <!-- Title Field -->
      <div class="mb-6">
        <label for="title" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Article Title</label>
        <input
          type="text"
          id="title"
          v-model="article.title"
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
          placeholder="Enter the article title"
          required
        />
      </div>

      <!-- Introduction Field -->
      <div class="mb-6">
        <label for="introduction" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Article Introduction</label>
        <input
          type="text"
          id="introduction"
          v-model="article.introduction"
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
          placeholder="Write a brief introduction"
          required
        />
      </div>

      <!-- Image Upload Field -->
      <div class="mb-6">
        <label for="image" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">Article Image</label>
        <input
          type="file"
          id="image"
          @change="handleImageUpload"
          accept="image/*"
          class="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
        />
        <p class="mt-1 text-sm text-gray-500 dark:text-gray-400" id="file_input_help">SVG, PNG, JPG or GIF.</p>
        <img
          v-if="article.imagePreview"
          :src="article.imagePreview"
          alt="Article Image Preview"
          class="mt-4 w-full h-48 object-cover rounded-lg"
        />
      </div>

      <!-- Editor -->
      <label for="image" class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">The Article</label>
      <WYSIWYG ref="wysiwygEditor" />

      <!-- Submit Button -->
      <br>
      <button
        id="send"
        type="submit"
        class="w-full bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 dark:bg-blue-700 dark:hover:bg-blue-800"
      >
        Save
      </button>
    </form>
  </div>
</template>

<script>
import api from '@/api';
import WYSIWYG from '@/utils/WYSIWYG.vue';
export default {
  components: {
    WYSIWYG
  },
  data() {
    return {
      article: {
        title: '',
        introduction: '',
        image: null,
        imagePreview: ''
      },
      saved: false
    };
  },
  methods: {
    handleImageUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.article.image = file;
        this.article.imagePreview = URL.createObjectURL(file);
      }
    },
    async saveArticle() {
      const editorContent = this.$refs.wysiwygEditor.editor.getHTML();
      const formData = new FormData();
      formData.append('content', editorContent);
      formData.append('title', this.article.title);
      formData.append('introduction', this.article.introduction);
      formData.append('thumbnail', this.article.image);

      try {
        const response = await api.post('app/article/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });

        if (response.status === 200 || response.status === 201) {
          this.saved = true;
          this.$router.push({ name: 'Dashboard' });
        }
      } catch (error) {
        console.error('Error saving the article:', error);
      }
    }
  }
};
</script>
