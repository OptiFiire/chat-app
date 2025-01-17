<template>
    <div class="w-full py-2 mx-auto flex flex-col gap-x-2">
        <div class="flex gap-4">
            <AvatarComponent :src="data.sender.avatar" size="10"/>
            <div class="flex flex-col">
                <div class="flex gap-3 font-medium items-end">
                    <p class="text-md">{{ data.sender.name }}</p>
                    <p class="text-xs text-neutral-700">
                        {{ new Date(data.created_at).toLocaleString() }}
                    </p>
                </div>
                <p class="mb-1.5 text-sm font-normal text-neutral-200">
                    {{ data.content }}
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
defineOptions({
    name: "MessageComponent"
})

defineProps({
    data: Object
})
</script>