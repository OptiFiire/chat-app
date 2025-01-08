<template>
    <DropdownMenu>
        <DropdownMenuTrigger class="h-9">
            <Button variant="secondary" size="icon" class="rounded-full">
                <Avatar v-if="user.avatar">
                    <AvatarImage :src="user.avatar" />
                    <AvatarFallback>{{ user.name }}</AvatarFallback>
                </Avatar>
                <CircleUser v-else class="h-5 w-5" />
            </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="rounded-xl min-w-40" align="end">
            <div class="p-2 flex gap-2">
                <div>
                    <Avatar v-if="user.avatar">
                        <AvatarImage :src="user.avatar" />
                        <AvatarFallback>{{ user.name }}</AvatarFallback>
                    </Avatar>
                    <CircleUser v-else class="h-5 w-5" />
                </div>
                <div class="flex flex-col">
                    <span class="text-md text-white ml-1">{{ user.name }}</span>
                    <span class="text-sm text-neutral-500 ml-1">{{ user.username }}</span>
                </div>
            </div>
            <DropdownMenuSeparator />
            <DropdownMenuItem @click="handleLogout" class="rounded-xl text-red-500 focus:bg-red-500/80 cursor-pointer">
                <LogOut class="ml-1" /> Log out
            </DropdownMenuItem>
        </DropdownMenuContent>
    </DropdownMenu>
</template>

<script setup lang="ts">
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
    DropdownMenuSeparator
} from '@/components/ui/dropdown-menu'
import { CircleUser, LogOut } from 'lucide-vue-next';
import Button from './ui/button/Button.vue';
import { Avatar, AvatarImage } from './ui/avatar';
import AvatarFallback from './ui/avatar/AvatarFallback.vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();

const handleLogout = async () => {
    const token = localStorage.getItem("auth_token")
    try {
        if (token) {
            await axios('http://127.0.0.1:8000/auth/token/logout',
                {
                    method: 'POST',
                    headers: { Authorization: `Token ${token}` },
                })
            localStorage.removeItem("auth_token");
            router.push({ name: "login" })
        }
    } catch (e) {
        console.error(e);
    }
}

defineProps({
    user: {
        type: Object,
        required: true
    }
})

defineOptions({
    name: 'AccountDropdown',
})
</script>