<script setup>
import { Search, Plus } from 'lucide-vue-next'
import { onMounted, ref, reactive } from 'vue'
import axios from 'axios';
import { RouterView } from 'vue-router'
import { Separator } from '@/components/ui/separator'
import { useRouter, useRoute } from 'vue-router';
import {
    Sidebar,
    SidebarContent,
    SidebarGroup,
    SidebarGroupContent,
    SidebarHeader,
    SidebarInput,
    SidebarInset,
    SidebarMenu,
    SidebarMenuButton,
    SidebarMenuItem,
    SidebarProvider,
    SidebarRail,
    SidebarTrigger,
    SidebarGroupLabel,
    SidebarGroupAction
} from '@/components/ui/sidebar'


import {
    Tooltip,
    TooltipContent,
    TooltipProvider,
    TooltipTrigger
} from '@/components/ui/tooltip'


import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar'
import AccountDropdown from '@/components/AccountDropdown.vue'

const data = {
    directMessages: [
        { title: 'Marcus', lastActivityBy: "You", newMessages: 0, lastMessage: "Holy cow, no", url: '#', isActive: true, },
        { title: 'Emenem', lastActivityBy: "Emenem", newMessages: 2, lastMessage: "She has it", url: '#' },
        { title: 'Drake', lastActivityBy: "Drake", newMessages: 4, lastMessage: "Are you restarted?", url: '#' }
    ]
}

const user = reactive({
    avatar: '',
    name: '',
    email: '',
    biography: '',
    username: ''
});

const search = ref('');

onMounted(async () => {
    const token = localStorage.getItem('auth_token');
    if (token) {
        const response = await axios('http://127.0.0.1:8000/api/users/me/', {
            headers: { Authorization: `Token ${token}` },
        });
        Object.assign(user, response.data);
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

            <SidebarContent>
                <SidebarGroup>
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
                    <SidebarGroupContent>
                        <SidebarMenu class="flex gap-1 flex-col">
                            <a :href="item.url" v-for="item in data.directMessages" :key="item.title">
                                <SidebarMenuItem
                                    class="duration-100 flex gap-2 items-center hover:bg-white/10 rounded-2xl">
                                    <SidebarMenuButton class="h-max flex justify-between">
                                        <div class="flex gap-2 items-center justify-between w-full">
                                            <div class="flex gap-2 items-center">
                                                <Avatar class="w-[36px] h-[36px]">
                                                    <AvatarImage class="w-[36px]"
                                                        src="https://i.pinimg.com/236x/68/31/12/68311248ba2f6e0ba94ff6da62eac9f6.jpg" />
                                                    <AvatarFallback>CN</AvatarFallback>
                                                </Avatar>
                                                <div class="flex flex-col">
                                                    <p class="max-w-40 truncate">{{ item.title }}</p>
                                                    <p class="max-w-32 text-neutral-500 truncate">
                                                        {{ item.lastActivityBy + ': ' + item.lastMessage }}
                                                    </p>
                                                </div>
                                            </div>
                                            <div
                                                class="bg-neutral-200 text-neutral-950 size-[20px] text-[10px] text-center px-0 py-0 rounded-full">
                                                {{ item.newMessages }}</div>
                                        </div>
                                    </SidebarMenuButton>
                                </SidebarMenuItem>
                            </a>
                        </SidebarMenu>
                    </SidebarGroupContent>
                </SidebarGroup>
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
                <AccountDropdown :user="user" />
            </header>

            <div class="flex flex-col h-full m-4 justify-center items-center">
                <router-view />
            </div>
        </SidebarInset>
    </SidebarProvider>
</template>