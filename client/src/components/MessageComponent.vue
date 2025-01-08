<template>
    <div class="max-w-4xl py-2 px-4 sm:px-6 lg:px-8 mx-auto flex gap-x-2 sm:gap-x-4">
        <div>
            <Avatar class="w-10 h-10">
                <AvatarImage class="w-10" :src="data.avatar" />
            </Avatar>
            <div class="space-y-1.5">
                <p class="text-sm text-gray-800 dark:text-white">
                    <strong class="font-medium">{{ data.name }}</strong>
                </p>
                <p class="text-xs text-gray-800 dark:text-white">
                    <time>{{ data.avatar }}</time>
                </p>
            </div>
        </div>

        <p class="mb-1.5 text-sm text-gray-800 dark:text-white">
            {{ data.content }}
        </p>
    </div>
</template>

<script setup lang="ts">
defineOptions({
    name: "MessageComponent"
})

defineProps({
    data: {
        type: Object,
        required: true
    }
})
</script>