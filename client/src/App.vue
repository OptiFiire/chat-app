<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import AuthLayout from '@/layouts/AuthLayout.vue';
import DefaultLayout from '@/layouts/DefaultLayout.vue';

const router = useRouter();
const route = useRoute()

const layout = computed(() => {
  const layoutName = route.meta.layout || 'DefaultLayout';
  return layoutName === 'AuthLayout' ? AuthLayout : DefaultLayout
})

onMounted(async () => {
  try {
    const isAuthenticated = localStorage.getItem('auth_token') ? true : false;
    if (!isAuthenticated && route.meta.layout !== "AuthLayout") router.push({ name: 'login' })
  } catch (error) {
    console.error(error);
    router.push({ name: 'login' });
  }
});
</script>