import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const user = ref({})
  const setUser = (user_input) => {
    user.value = user_input
  }

  return { user, setUser }
})

