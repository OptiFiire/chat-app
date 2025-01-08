<template>
    <Card class="mx-auto max-w-sm rounded-2xl">
        <CardHeader>
            <CardTitle class="text-xl">
                Sign Up
            </CardTitle>
            <CardDescription>
                Enter your information to create an account
            </CardDescription>
        </CardHeader>
        <CardContent>
            <form @submit.prevent="onSubmit" class="grid gap-4">
                <div class="grid gap-2">
                    <Label for="email">Email</Label>
                    <Input v-model="email" id="email" type="email" class="rounded-2xl" placeholder="Enter email..."
                        required />
                </div>
                <div class="grid gap-2">
                    <Label for="username">Username</Label>
                    <Input v-model="username" id="username" type="text" class="rounded-2xl"
                        placeholder="Enter username..." required />
                </div>
                <div class="grid gap-2">
                    <Label for="password">Password</Label>
                    <Input v-model="password" id="password" type="password" class="rounded-2xl"
                        placeholder="Enter password..." required autocomplete />
                </div>
                <span v-if="loginError" class="text-red-500 text-sm">{{ loginError }}</span>
                <Button type="submit" class="rounded-2xl w-full">
                    Create an account
                </Button>
            </form>
            <div class="mt-4 text-center text-sm">
                Already have an account?
                <router-link :to="{ name: 'login' }" class="underline">
                    Log in
                </router-link>
            </div>
        </CardContent>
    </Card>
</template>

<script setup>
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { useForm, useField } from 'vee-validate'
import * as yup from 'yup'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { ref } from 'vue'

const schema = yup.object({
    username: yup.string().required('Username is required'),
    password: yup.string().required('Password is required'),
})

const { handleSubmit, errors } = useForm({
    validationSchema: schema,
})

const { value: username } = useField('username')
const { value: email } = useField('email')
const { value: password } = useField('password')

const router = useRouter()
const loginError = ref('')

const onSubmit = handleSubmit(async (values) => {
    try {
        const response = await axios.post('http://127.0.0.1:8000/auth/users/', values)
        const token = (await axios.post('http://127.0.0.1:8000/auth/token/login', values)).data.auth_token
        localStorage.setItem('auth_token', token)
        router.push({ name: 'home' })
    } catch (e) {
        loginError.value = e?.response?.data?.detail || 'An error occurred while trying to login.'
    }
})
</script>