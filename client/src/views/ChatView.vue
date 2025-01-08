<template>
    <div class="relative h-full flex items-center justify-center flex-col w-full">
        <div class="h-full flex flex-col justify-center items-center">
            <div class="bg-white/10 border flex flex-col justify-center items-center gap-6 border-white/20 rounded-2xl p-8">
                <p class="text-9xl">👋</p>
                <p class="font-medium text-xl sm:text-2xl text-center">Wave to <span class="text-yellow-600">{{ data.name }}</span></p>
            </div>
        </div>

        <div class="max-w-4xl w-full sticky bottom-1 z-10">
            <div class="relative flex gap-2">
                <Textarea class="max-h-24 bg-neutral-800 border-neutral-200/10" :placeholder="'Message to ' + data.name + '...'" />
                <button type="button"
                    class="inline-flex md:hidden shrink-0 justify-center items-center size-8 rounded-2xl text-white bg-blue-600 hover:bg-blue-500 focus:z-10 focus:outline-none focus:bg-blue-500">
                    <SendHorizontal class="w-4" />
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import Label from '@/components/ui/label/Label.vue';
import Textarea from '@/components/ui/textarea/Textarea.vue';
import { User, SendHorizontal } from 'lucide-vue-next';

const data = {
    name: 'John Doe'
}
</script>