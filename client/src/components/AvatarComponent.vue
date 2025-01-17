<template>
    <Avatar v-if="src">
        <AvatarImage :src="src.startsWith('http') ? src : 'http://127.0.0.1:8000' + src" />
        <AvatarFallback>{{ fallback }}</AvatarFallback>
    </Avatar>
    <CircleUser v-else class="h-10 w-10 p-1 bg-muted rounded-full border border-white/10" />
</template>

<script setup>
defineProps({
    size: String,
    src: String,
    fallback: String
})

defineOptions({
    name: 'AvatarComponent'
})
</script>