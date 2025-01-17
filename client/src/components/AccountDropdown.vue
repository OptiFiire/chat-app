<template>
    <DropdownMenu>
        <DropdownMenuTrigger>
            <Button variant="secondary" size="icon" class="rounded-full">
                <AvatarComponent :src="user.avatar" :fallback="user.name" />
            </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="rounded-xl min-w-40" align="end">
            <div class="p-2 flex gap-2">
                <AvatarComponent :src="user.avatar" :fallback="user.name" />
                <div class="flex flex-col">
                    <span class="text-md text-white ml-1">{{ user.name }}</span>
                    <span class="text-sm text-neutral-500 ml-1">@{{ user.username }}</span>
                </div>
            </div>
            <DropdownMenuSeparator />
            <DropdownMenuItem @click="handleLogout"
                class="rounded-xl text-red-500 focus:text-red-500 focus:bg-red-800/30 cursor-pointer">
                <LogOut class="ml-1" /> Log out
            </DropdownMenuItem>
        </DropdownMenuContent>
    </DropdownMenu>
</template>

<script setup>
import { useUserStore } from '@/misc/store';
import { useRouter } from 'vue-router';
import axios from '@/misc/axios';
import { ref } from 'vue';

const user = ref(useUserStore().user)
const router = useRouter()

const handleLogout = async () => {
    try {
        await axios.post('/auth/token/logout')
        localStorage.removeItem("auth_token")
        router.push({ name: "login" })
    } catch (e) {
        console.error(e);
    }
}

defineOptions({
    name: 'AccountDropdown',
})
</script>