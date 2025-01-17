<template>
  <Card class="mx-auto max-w-sm rounded-2xl">
    <CardHeader>
      <CardTitle class="text-2xl">
        Login
      </CardTitle>
      <CardDescription>
        Enter your email below to login to your account
      </CardDescription>
    </CardHeader>
    <CardContent>
      <form @submit.prevent="onSubmit" class="grid gap-4">
        <div class="grid gap-2">
          <Label for="username">Username</Label>
          <Input v-model="username" id="username" type="text" placeholder="Enter your username..." required
            autocomplete="true" class="rounded-2xl" />
        </div>
        <div class="grid gap-2">
          <div class="flex items-center">
            <Label for="password">Password</Label>
            <a href="#" class="ml-auto inline-block text-sm underline">
              Forgot your password?
            </a>
          </div>
          <Input v-model="password" id="password" type="password" placeholder="Enter your password..." required
            autocomplete="true" class="rounded-2xl" />
        </div>
        <span v-if="loginError" class="text-red-500 text-sm">{{ loginError }}</span>
        <Button type="submit" class="w-full rounded-2xl">
          Login
        </Button>
      </form>
      <div class="mt-4 text-center text-sm">
        Don't have an account?
        <router-link :to="{ name: 'signup' }" class="underline">
          Sign up
        </router-link>
      </div>
    </CardContent>
  </Card>
</template>

<script setup>
import { useForm, useField } from 'vee-validate'
import { useRouter } from 'vue-router'
import { ref } from 'vue'

import axios from '@/misc/axios'
import * as yup from 'yup'


const router = useRouter()
const loginError = ref('')

const schema = yup.object({
  username: yup.string().required('Username is required'),
  password: yup.string().required('Password is required'),
})

const { handleSubmit, errors } = useForm({
  validationSchema: schema
})

const { value: username } = useField('username')
const { value: password } = useField('password')

const onSubmit = handleSubmit(async (credentials) => {  
  try {
    const fetchToken = await axios.post('/auth/token/login', credentials)
    localStorage.setItem('auth_token', fetchToken.data.auth_token)
    router.push({ name: 'home' })
  } catch (e) {
    console.error(e)
    loginError.value = e.response.data.non_field_errors[0] || 'An error occurred while trying to login.'
  }
})
</script>