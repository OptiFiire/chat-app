<template>
    <div class="flex w-full h-full gap-4">
        <div class="relative h-full flex items-center justify-center flex-col w-full p-4">
            <div class="h-full w-full flex flex-col justify-center items-center">
                <div v-if="messages.length === 0"
                    class="bg-white/10 border flex flex-col justify-center items-center gap-6 border-white/20 rounded-2xl p-8">
                    <p class="text-9xl">👋</p>
                    <p class="font-medium text-xl sm:text-2xl text-center">
                        Wave to <span class="text-sky-600">{{ partner.name }}</span>
                    </p>
                </div>
                <div class="w-full h-full flex flex-col justify-end items-end mb-4" v-else>
                    <MessageComponent v-for="item in messages" :key="item.id" :data="item" />
                </div>
            </div>

            <div class="w-full sticky bottom-1 z-10">
                <div class="relative flex gap-2">
                    <Textarea v-model="message" @send="sendMessage" @newline="insertNewline"
                        class="max-h-24 bg-muted/50 border-muted" :placeholder="'Message to ' + partner.name + '...'" />
                    <button type="submit"
                        class="inline-flex md:hidden shrink-0 justify-center items-center size-8 rounded-lg text-white bg-primary focus:z-10 focus:outline-none">
                        <SendHorizontal class="w-4" />
                    </button>
                </div>
            </div>
        </div>
        <div class="relative h-full hidden lg:flex w-[550px] flex-col bg-background border-l">
            <div class="flex flex-col justify-center">
                <div class="bg-white w-full h-24" />
                <div class="absolute top-14 w-full flex justify-center">
                    <Avatar v-if="partner.avatar">
                        <AvatarImage :src="'http://127.0.0.1:8000' + partner.avatar" />
                        <AvatarFallback>{{ partner.name }}</AvatarFallback>
                    </Avatar>
                    <CircleUser v-else class="h-20 w-20 p-1 bg-muted rounded-full border border-white/10" />
                </div>
            </div>
            <div class="w-full flex items-center flex-col mt-12">
                <p class="text-2xl font-medium">{{ partner.name }}</p>
                <p class="text-md font-normal text-primary-foreground/50">@{{ partner.username }}</p>
            </div>
            <div class="bg-muted rounded-2xl m-4 flex justify-center items-center flex-col">
                <div v-if="partner.biography" class="p-4 w-full space-y-1">
                    <p class="text-sm font-medium">Biography</p>
                    <p class="text-sm flex items-center gap-2 text-primary-foreground">{{ partner.biography }}</p>
                </div>
                <Separator v-if="partner.biography" class="bg-primary-foreground w-[90%]" />
                <div class="p-4 w-full">
                    <p class="text-sm font-medium">Date Joined</p>
                    <p class="text-sm flex items-center gap-2 text-primary-foreground/40">
                        {{ new Date(partner.date_joined).toDateString() }}
                    </p>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>
import { onMounted, reactive, ref, watch } from 'vue'
import { useUserStore } from "@/misc/store"
import { useRoute } from 'vue-router'
import axios from '@/misc/axios'

const message = ref('')

const route = useRoute()
const user = useUserStore()

const messages = ref([])
const partner = reactive({})

const sendMessage = async () => {
    if (!message.value.trim()) return

    try {
        const response = await axios.post(`/api/messages/`,
            { content: message.value, receiver: partner, }
        );

        message.value = '';
        messages.value.push({
            id: response.data.id,
            content: response.data.content,
            sender: user,
            created_at: response.data.timestamp,
        });
    }
    catch (error) {
        console.error(error);
    }
}

const insertNewline = () => {
    message.value += '\n';
};

const fetchChatData = async (chatId) => {
    try {
        const [messagesResponse, chatResponse] = await Promise.all([
            axios.get(`/api/chats/${chatId}/messages`),
            axios.get(`/api/chats/${chatId}`),
        ]);

        messages.value = messagesResponse.data;
        Object.assign(partner, chatResponse.data.partner);
    } catch (error) {
        console.error(error);
    }
};

watch(
    () => route.params.chatId,
    (newChatId) => {
        fetchChatData(newChatId);
    },
);

onMounted(async () => {
    fetchChatData(route.params.chatId);
})
</script>