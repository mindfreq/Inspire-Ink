<template>
  <div class=" border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600 p-4">
    <!-- شريط الأدوات -->
    <div class="px-3 py-2 border-b border-gray-200 dark:border-gray-600">
      <div class="flex flex-wrap items-center">
        <div class="flex items-center space-x-1 rtl:space-x-reverse flex-wrap">
          <!-- RTL & LTR -->
          <button
            @click="toggleRTL"
            type="button"
            data-tooltip-target="tooltip-rtl"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16M13 12l3-3m0 0 3 3m-3-3v12"/>
            </svg>
            <span class="sr-only">RTL</span>
          </button>
          <div id="tooltip-rtl" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            RTL
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <button
            @click="toggleLTR"
            type="button"
            data-tooltip-target="tooltip-ltr"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h8m4-6 3 3m0 0-3 3m3-3H13"/>
            </svg>
            <span class="sr-only">LTR</span>
          </button>
          <div id="tooltip-ltr" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            LTR
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Bold Button -->
          <button
            @click="toggleBold"
            type="button"
            data-tooltip-target="tooltip-bold"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5h4.5a3.5 3.5 0 1 1 0 7H8m0-7v7m0-7H6m2 7h6.5a3.5 3.5 0 1 1 0 7H8m0-7v7m0 0H6"/>
            </svg>
            <span class="sr-only">Bold</span>
          </button>
          <div id="tooltip-bold" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Bold
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Italic Button -->
          <button
            @click="toggleItalic"
            type="button"
            data-tooltip-target="tooltip-italic"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m8.874 19 6.143-14M6 19h6.33m-.66-14H18"/>
            </svg>
            <span class="sr-only">Italic</span>
          </button>
          <div id="tooltip-italic" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Italic
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Underline Button -->
          <button
            @click="toggleUnderline"
            type="button"
            data-tooltip-target="tooltip-underline"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M6 19h12M8 5v9a4 4 0 0 0 8 0V5M6 5h4m4 0h4"/>
            </svg>
            <span class="sr-only">Underline</span>
          </button>
          <div id="tooltip-underline" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Underline
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Strike Button -->
          <button
            @click="toggleStrike"
            type="button"
            data-tooltip-target="tooltip-strike"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 6.2V5h12v1.2M7 19h6m.2-14-1.677 6.523M9.6 19l1.029-4M5 5l6.523 6.523M19 19l-7.477-7.477"/>
            </svg>
            <span class="sr-only">Strike</span>
          </button>
          <div id="tooltip-strike" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Strike
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Highlight Button -->
          <button
            @click="toggleHighlight"
            type="button"
            data-tooltip-target="tooltip-highlight"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M9 19.2H5.5c-.3 0-.5-.2-.5-.5V16c0-.2.2-.4.5-.4h13c.3 0 .5.2.5.4v2.7c0 .3-.2.5-.5.5H18m-6-1 1.4 1.8h.2l1.4-1.7m-7-5.4L12 4c0-.1 0-.1 0 0l4 8.8m-6-2.7h4m-7 2.7h2.5m5 0H17"/>
            </svg>
            <span class="sr-only">Highlight</span>
          </button>
          <div id="tooltip-highlight" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Highlight
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Code Button -->
          <button
            @click="toggleCode"
            type="button"
            data-tooltip-target="tooltip-code"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m8 8-4 4 4 4m8 0 4-4-4-4m-2-3-4 14"/>
            </svg>
            <span class="sr-only">Code</span>
          </button>
          <div id="tooltip-code" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Code
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Link Button -->
          <button
            @click="toggleLink"
            type="button"
            data-tooltip-target="tooltip-link"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.213 9.787a3.391 3.391 0 0 0-4.795 0l-3.425 3.426a3.39 3.39 0 0 0 4.795 4.794l.321-.304m-.321-4.49a3.39 3.39 0 0 0 4.795 0l3.424-3.426a3.39 3.39 0 0 0-4.794-4.795l-1.028.961"/>
            </svg>
            <span class="sr-only">Link</span>
          </button>
          <div id="tooltip-link" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Link
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Remove Link Button -->
          <button
            @click="removeLink"
            type="button"
            data-tooltip-target="tooltip-remove-link"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M13.2 9.8a3.4 3.4 0 0 0-4.8 0L5 13.2A3.4 3.4 0 0 0 9.8 18l.3-.3m-.3-4.5a3.4 3.4 0 0 0 4.8 0L18 9.8A3.4 3.4 0 0 0 13.2 5l-1 1m7.4 14-1.8-1.8m0 0L16 16.4m1.8 1.8 1.8-1.8m-1.8 1.8L16 20"/>
            </svg>
            <span class="sr-only">Remove link</span>
          </button>
          <div id="tooltip-remove-link" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Remove link
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Image Button -->
          <button
            @click="insertImage"
            type="button"
            data-tooltip-target="tooltip-image"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 19h14a1 1 0 0 0 .9-1.45L14 7l-4.9 9.55a1 1 0 0 1-.9.45H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1Z"/>
            </svg>
            <span class="sr-only">Insert Image</span>
          </button>
          <div id="tooltip-image" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Insert Image
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>
          <!-- Text Size Dropdown -->
          <div class="relative">
              <button
                @click="toggleTextSizeDropdown"
                type="button"
                data-tooltip-target="tooltip-text-size"
                class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
              >
                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6.2V5h11v1.2M8 5v14m-3 0h6m2-6.8V11h8v1.2M17 11v8m-1.5 0h3"/>
                </svg>
                <span class="sr-only">Text size</span>
              </button>
              <div v-if="isTextSizeDropdownOpen" class="absolute z-10 mt-2 bg-white rounded-lg shadow-lg dark:bg-gray-700">
                <ul class="py-1">
                  <li
                    v-for="size in textSizes"
                    :key="size"
                    @click="setTextSize(size)"
                    class="px-4 py-2 text-sm text-gray-700 cursor-pointer hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600"
                  >
                    {{ size }}
                  </li>
                </ul>
              </div>
            </div>

            <!-- Font Family Dropdown -->
            <div class="relative">
              <button
                @click="toggleFontFamilyDropdown"
                type="button"
                data-tooltip-target="tooltip-font-family"
                class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
              >
                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m10.6 19 4.298-10.93a.11.11 0 0 1 .204 0L19.4 19m-8.8 0H9.5m1.1 0h1.65m7.15 0h-1.65m1.65 0h1.1m-7.7-3.985h4.4M3.021 16l1.567-3.985m0 0L7.32 5.07a.11.11 0 0 1 .205 0l2.503 6.945h-5.44Z"/>
                </svg>
                <span class="sr-only">Font family</span>
              </button>
              <div v-if="isFontFamilyDropdownOpen" class="absolute z-10 mt-2 bg-white rounded-lg shadow-lg dark:bg-gray-700">
                <ul class="py-1">
                  <li
                    v-for="font in fontFamilies"
                    :key="font"
                    @click="setFontFamily(font)"
                    class="px-4 py-2 text-sm text-gray-700 cursor-pointer hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-600"
                  >
                    {{ font }}
                  </li>
                </ul>
              </div>
            </div>

          <!-- Divider -->
          <div class="px-1">
            <span class="block w-px h-4 bg-gray-300 dark:bg-gray-600"></span>
          </div>

          <!-- Align Left Button -->
          <button
            @click="setTextAlign('left')"
            type="button"
            data-tooltip-target="tooltip-align-left"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 6h8m-8 4h12M6 14h8m-8 4h12"/>
            </svg>
            <span class="sr-only">Align left</span>
          </button>
          <div id="tooltip-align-left" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Align left
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Align Center Button -->
          <button
            @click="setTextAlign('center')"
            type="button"
            data-tooltip-target="tooltip-align-center"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 6h8M6 10h12M8 14h8M6 18h12"/>
            </svg>
            <span class="sr-only">Align center</span>
          </button>
          <div id="tooltip-align-center" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Align center
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>

          <!-- Align Right Button -->
          <button
            @click="setTextAlign('right')"
            type="button"
            data-tooltip-target="tooltip-align-right"
            class="p-1.5 text-gray-500 rounded-sm cursor-pointer hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-600"
          >
            <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 6h-8m8 4H6m12 4h-8m8 4H6"/>
            </svg>
            <span class="sr-only">Align right</span>
          </button>
          <div id="tooltip-align-right" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
            Align right
            <div class="tooltip-arrow" data-popper-arrow></div>
          </div>
        </div>
      </div>
    </div>

    <!-- المحرر -->
    <div class="px-4 py-2 bg-white rounded-b-lg dark:bg-gray-800">
      <editor-content :editor="editor" />
    </div>
  </div>
</template>
<script>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { Editor, EditorContent } from '@tiptap/vue-3';
import StarterKit from '@tiptap/starter-kit';
import Highlight from '@tiptap/extension-highlight';
import Underline from '@tiptap/extension-underline';
import Link from '@tiptap/extension-link';
import TextAlign from '@tiptap/extension-text-align';
import Image from '@tiptap/extension-image';
import YouTube from '@tiptap/extension-youtube';
import TextStyle from '@tiptap/extension-text-style';
import FontFamily from '@tiptap/extension-font-family';
import { Color } from '@tiptap/extension-color';
import FontSize from '@tiptap/extension-font-size';

export default {
  components: {
    EditorContent,
  },
  setup() {
    const editor = ref(null);
    const isTextSizeDropdownOpen = ref(false);
    const isTextColorDropdownOpen = ref(false);
    const isFontFamilyDropdownOpen = ref(false);
    const selectedColor = ref('#000000');
    const textSizes = ['12px', '14px', '16px', '18px', '24px', '36px'];
    const fontFamilies = ['Arial', 'Courier New', 'Georgia', 'Times New Roman', 'Verdana'];

    onMounted(() => {
      editor.value = new Editor({
        extensions: [
          StarterKit,
          Highlight,
          Underline,
          Link,
          TextAlign.configure({
            types: ['heading', 'paragraph'],
          }),
          Image,
          YouTube,
          TextStyle,
          FontFamily,
          Color,
          FontSize.configure({
            defaultSize: '18px',
          }),
    ],
        content: '<p style="font-size: 18px;">Write here ...</p>',
      });
    });

    onBeforeUnmount(() => {
      editor.value.destroy();
    });

    const toggleRTL = () => {
      editor.value.chain().focus().setTextAlign('right').run();
      document.querySelector('.ProseMirror').style.direction = 'rtl';
    };

    const toggleLTR = () => {
      editor.value.chain().focus().setTextAlign('left').run();
      document.querySelector('.ProseMirror').style.direction = 'ltr';
    };

    const toggleBold = () => editor.value.chain().focus().toggleBold().run();
    const toggleItalic = () => editor.value.chain().focus().toggleItalic().run();
    const toggleUnderline = () => editor.value.chain().focus().toggleUnderline().run();
    const toggleStrike = () => editor.value.chain().focus().toggleStrike().run();
    const toggleHighlight = () => editor.value.chain().focus().toggleHighlight().run();
    const toggleCode = () => editor.value.chain().focus().toggleCode().run();
    const toggleLink = () => {
      const url = window.prompt('Enter URL');
      editor.value.chain().focus().toggleLink({ href: url }).run();
    };
    const removeLink = () => editor.value.chain().focus().unsetLink().run();
    const setTextAlign = (align) => editor.value.chain().focus().setTextAlign(align).run();
    const setTextSize = (size) => {
    editor.value.chain().focus().setFontSize(size).run();
    isTextSizeDropdownOpen.value = false;
  };
    const setTextColor = () => editor.value.chain().focus().setColor(selectedColor.value).run();
    const resetTextColor = () => editor.value.chain().focus().unsetColor().run();
    const setFontFamily = (font) => {
      editor.value.chain().focus().setFontFamily(font).run();
      isFontFamilyDropdownOpen.value = false;
    };

    const toggleTextSizeDropdown = () => isTextSizeDropdownOpen.value = !isTextSizeDropdownOpen.value;
    const toggleTextColorDropdown = () => isTextColorDropdownOpen.value = !isTextColorDropdownOpen.value;
    const toggleFontFamilyDropdown = () => isFontFamilyDropdownOpen.value = !isFontFamilyDropdownOpen.value;
    const insertImage = () => {
    const url = window.prompt('Enter the image URL'); 
    if (url) {
      editor.value.chain().focus().setImage({ src: url }).run(); 
    }
    
};
    return {
      editor,
      isTextSizeDropdownOpen,
      isTextColorDropdownOpen,
      isFontFamilyDropdownOpen,
      selectedColor,
      textSizes,
      fontFamilies,
      toggleRTL,
      toggleLTR,
      toggleBold,
      toggleItalic,
      toggleUnderline,
      toggleStrike,
      toggleHighlight,
      toggleCode,
      toggleLink,
      removeLink,
      setTextAlign,
      setTextSize,
      setTextColor,
      resetTextColor,
      setFontFamily,
      toggleTextSizeDropdown,
      toggleTextColorDropdown,
      toggleFontFamilyDropdown,
      insertImage,
    };
  },
};
</script>
