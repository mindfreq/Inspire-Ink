<template class="bg-white text-black dark:bg-gray-900 dark:text-white">
  <div id="app">


    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',
}
import { onMounted } from 'vue'
import { 
    initAccordions, 
    initCarousels, 
    initCollapses, 
    initDials, 
    initDismisses, 
    initDrawers, 
    initDropdowns, 
    initModals, 
    initPopovers, 
    initTabs, 
    initTooltips } from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
    initAccordions();
    initCarousels();
    initCollapses();
    initDials();
    initDismisses();
    initDrawers();
    initDropdowns();
    initModals();
    initPopovers();
    initTabs();
    initTooltips();
})

</script>

<style>
/* يمكنك إضافة أنماط مخصصة هنا إذا لزم الأمر */
</style>