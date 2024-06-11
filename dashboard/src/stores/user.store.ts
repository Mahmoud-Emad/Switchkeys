import { defineStore } from 'pinia'

import type { ISignUpResponse } from '../utils/types'

export const useUserStore = defineStore('user', {
  state: (): ISignUpResponse => {
    return {
      id: 0,
      email: '',
      first_name: '',
      last_name: '',
      password: '',
      access_token: '',
      refresh_token: '',
      joining_at: '',
      user_type: '',
    }
  },
  actions: {
    set(userResponse: ISignUpResponse) {
      this.id = userResponse.id
      this.email = userResponse.email
      this.first_name = userResponse.first_name
      this.last_name = userResponse.last_name
      this.password = userResponse.password
      this.access_token = userResponse.access_token
      this.refresh_token = userResponse.refresh_token
      this.joining_at = userResponse.joining_at
      this.user_type = userResponse.user_type
    },
  },
})
