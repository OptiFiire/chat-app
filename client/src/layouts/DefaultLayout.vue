<script setup>
import { useUserStore } from '@/misc/store';
import { onMounted, ref } from 'vue'
import axios from '@/misc/axios';

const user = useUserStore();
const search = ref('');
const chats = ref([])

onMounted(async () => {
    try {
        const fetchedUser = await axios('/api/users/me/')
        const fetchedChats = await axios('/api/chats/')
        user.setUser(fetchedUser.data)
        chats.value = fetchedChats.data
    } catch (e) {
        console.error(e);
    }
});
</script>

<template>
    <SidebarProvider>
        <Sidebar>
            <SidebarHeader>
                <div class="relative w-full max-w-sm items-center">
                    <SidebarInput :ref="search" id="search" v-model="search" placeholder="Search direct messages..."
                        class="pl-8 rounded-2xl h-10" />
                    <span class="absolute start-0 inset-y-0 flex items-center justify-center px-3">
                        <Search class="size-4 text-muted-foreground" />
                    </span>
                </div>
            </SidebarHeader>

            <SidebarContent :class="chats.length > 0 ? null : 'flex justify-center items-center'">
                <SidebarGroup v-if="chats.length > 0">
                    <SidebarGroupLabel>Direct Messages</SidebarGroupLabel>
                    <SidebarGroupAction>
                        <TooltipProvider>
                            <Tooltip>
                                <TooltipTrigger>
                                    <Plus class="w-3" />
                                </TooltipTrigger>
                                <TooltipContent>
                                    <p>Create a DM</p>
                                </TooltipContent>
                            </Tooltip>
                        </TooltipProvider>
                    </SidebarGroupAction>
                    <SidebarGroupContent v-if="chats.length > 0">
                        <SidebarMenu class="flex gap-1 flex-col">
                            <router-link class="duration-100" active-class="bg-white/5 rounded-2xl"
                                v-for="item in chats" :key="item.id"
                                :to="{ name: 'chat', params: { chatId: item.id } }">
                                <SidebarMenuItem
                                    class="duration-100 flex gap-2 items-center hover:bg-white/10 rounded-2xl">
                                    <SidebarMenuButton class="h-max flex justify-between">
                                        <div class="flex gap-2 items-center justify-between w-full">
                                            <div class="flex gap-2 items-center">
                                                <AvatarComponent :src="item.partner.avatar"
                                                    :fallback="item.partner.name" />
                                                <div class="flex flex-col">
                                                    <p class="max-w-40 truncate text-start">{{ item.partner.name }}</p>
                                                    <p v-if="item.last_message"
                                                        class="max-w-40 text-neutral-500 truncate">
                                                        {{ item.last_message.sender.id == user.id
                                                            ? 'You'
                                                            : item.last_message.sender.name }}: {{ item.last_message.content
                                                        }}
                                                    </p>
                                                </div>
                                            </div>
                                            <div v-if="item.unread_messages_count > 0"
                                                class="bg-neutral-200 text-neutral-950 font-bold size-[20px] text-[10px] text-center px-0 py-0 rounded-full">
                                                {{ item.unread_messages_count }}</div>
                                        </div>
                                    </SidebarMenuButton>
                                </SidebarMenuItem>
                            </router-link>
                        </SidebarMenu>
                    </SidebarGroupContent>
                </SidebarGroup>
                <p v-else class="text-neutral-500 text-center">No direct messages found.</p>
            </SidebarContent>
            <SidebarRail />
        </Sidebar>

        <SidebarInset>
            <header class="flex h-16 shrink-0 items-center justify-between gap-2 border-b px-4">
                <div class="flex items-center gap-2">
                    <SidebarTrigger />
                    <Separator orientation="vertical" class="mx-1 h-4" />
                    <h1>Chat App</h1>
                </div>
                <AccountDropdown />
            </header>
            <div class="flex flex-col h-full justify-center items-center">
                <router-view />
            </div>
        </SidebarInset>

    </SidebarProvider>
</template>