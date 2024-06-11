<template>
  <v-dialog
    persistent
    transition="dialog-bottom-transition"
    v-model="$props.openDialog"
    width="1600"
  >
    <v-card class="signup-card" height="900">
      <v-row>
        <v-col cols="6" class="d-flex justify-center align-center pa-10">
          <v-img src="/images/auth/signup_logo.png" class="signup-image" />
        </v-col>
        <v-col cols="6" class="d-flex justify-center pa-10">
          <v-row>
            <v-col cols="12" class="d-flex align-center">
              <div class="w-100">
                <h1>Get started</h1>
                <small class="text-gray">
                  It looks like you're new to our dashboard. You can easily sign
                  up using one of our authentication methods.
                </small>
              </div>
            </v-col>
            <v-col cols="12" class="d-flex align-center">
              <div class="w-100">
                <v-form v-model="isValidForm">
                  <v-text-field
                    v-for="input in formInputs"
                    :key="input.label"
                    v-model="input.vModel.value"
                    :type="input.type.value"
                    :label="input.label"
                    :rules="input.rules"
                    :aria-label="input.label"
                    variant="outlined"
                    autocomplete
                    hide-details="auto"
                    class="mb-4"
                    color="primary"
                    style="color: white"
                  >
                    <template #append-inner>
                      <v-icon
                        v-if="input.label.toLowerCase() === 'password'"
                        :color="getIconColor(input.label)"
                        style="cursor: pointer"
                        @click="toggleShowPassword"
                      >
                        {{ showPassword ? 'mdi-eye' : 'mdi-eye-off' }}
                      </v-icon>
                    </template>

                    <template #prepend>
                      <v-icon :color="getIconColor(input.label)">
                        {{ input.icon }}
                      </v-icon>
                    </template>
                  </v-text-field>
                </v-form>
                <v-alert
                  v-if="errorMessage || successMessage"
                  :type="errorMessage ? 'error' : 'success'"
                  variant="tonal"
                >
                  {{ errorMessage || successMessage }}
                </v-alert>
                <div class="ml-10">
                  <p class="mt-4 mb-2">Please keep in mind:</p>
                  <ul style="color: blue">
                    <li v-for="(hint, index) in passwordHints" :key="index">
                      <small class="text-white">{{ hint }}</small>
                    </li>
                  </ul>
                </div>
                <p class="mt-2">
                  You can easily click the
                  <span
                    class="generate-password-span text-primary"
                    @click="internalGenerateStrongPassword"
                  >
                    Generate Strong Password
                  </span>
                  to create a secure password for you.
                </p>
              </div>
            </v-col>
            <v-col cols="12" class="d-flex align-end">
              <v-col cols="12" class="d-flex justify-end">
                <v-btn
                  variant="flat"
                  color="primary"
                  class="ml-2 mr-2 pa-5 d-flex align-center justify-center"
                  :disabled="!isValidForm || isLoadingSignUp"
                  :loading="isLoadingSignUp"
                  @click="signup"
                  aria-label="Sign Up"
                >
                  Sign Up
                </v-btn>
              </v-col>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import axios from 'axios'
import { computed, defineComponent, ref } from 'vue'

import { useUserStore } from '../../stores/user.store'
import { generateStrongPassword } from '../../utils/generators'
import type { ISignUpResponse, SignUpFormInputs } from '../../utils/types'
import {
  isStrongPasswordRules,
  isValidEmailRules,
  isValidNameRules,
} from '../../utils/validators'

export default defineComponent({
  name: 'SignUpComponent',
  props: {
    openDialog: {
      type: Boolean,
      required: true,
    },
  },
  emits: ['update:close-dialog'],
  setup(props, { emit }) {
    const showPassword = ref(false)
    const isValidForm = ref(false)
    const isLoadingSignUp = ref(false)
    const errorMessage = ref<string>()
    const successMessage = ref<string>()

    const passwordEyeIconColor = computed(() =>
      isStrongPasswordRules(password.value) === true ? 'primary' : 'error'
    )
    const emailIconColor = computed(() =>
      isValidEmailRules(email.value) === true ? 'primary' : 'error'
    )
    const fNameIconColor = computed(() =>
      isValidNameRules(fName.value) === true ? 'primary' : 'error'
    )
    const lNameIconColor = computed(() =>
      isValidNameRules(lName.value) === true ? 'primary' : 'error'
    )

    const email = ref<string>('')
    const fName = ref<string>('')
    const lName = ref<string>('')
    const password = ref<string>('')

    const TOKENS_KEY = import.meta.env.VITE_SWITCHKEYS_TOKENS
    const SERVER_URL = import.meta.env.VITE_SERVER_URL

    const passwordHints = [
      'The password should be strong.',
      'Use at least 8 characters.',
      'Include both uppercase and lowercase letters.',
      'Add numbers and special characters (e.g., @, #, $, %, etc.).',
      'Avoid using easily guessable information like your name or birthdate.',
    ]

    const signup = async () => {
      try {
        errorMessage.value = undefined
        successMessage.value = undefined
        isLoadingSignUp.value = true

        const payload = {
          email: email.value,
          first_name: fName.value,
          last_name: lName.value,
          password: password.value,
        }

        const response = await axios.post(`${SERVER_URL}/auth/signup/`, payload)
        successMessage.value = response.data.message

        const results: ISignUpResponse = response.data.results
        localStorage.setItem(
          TOKENS_KEY,
          JSON.stringify({
            access: results.access_token,
            refresh: results.refresh_token,
          })
        )

        const userStore = useUserStore()
        userStore.set(results)

        setTimeout(() => emit('update:close-dialog'), 1500)
      } catch (error: any) {
        errorMessage.value = error.response?.data?.message || error.message
      } finally {
        isLoadingSignUp.value = false
      }
    }

    const toggleShowPassword = () => {
      showPassword.value = !showPassword.value
      setTimeout(() => {
        showPassword.value = !showPassword.value
      }, 1000)
    }

    const internalGenerateStrongPassword = () => {
      password.value = generateStrongPassword()
      showPassword.value = true
      setTimeout(() => {
        showPassword.value = false
      }, 1000)
    }

    const formInputs: SignUpFormInputs[] = [
      {
        vModel: email,
        icon: 'mdi-at',
        label: 'Email',
        rules: [isValidEmailRules],
        type: ref('email'),
      },
      {
        vModel: fName,
        icon: 'mdi-account',
        label: 'First Name',
        rules: [isValidNameRules],
        type: ref('text'),
      },
      {
        vModel: lName,
        icon: 'mdi-account',
        label: 'Last Name',
        rules: [isValidNameRules],
        type: ref('text'),
      },
      {
        vModel: password,
        icon: 'mdi-lock',
        label: 'Password',
        rules: [isStrongPasswordRules],
        type: computed(() => (showPassword.value ? 'text' : 'password')),
      },
    ]

    const getIconColor = (label: string) => {
      switch (label.toLowerCase()) {
        case 'email':
          return emailIconColor.value
        case 'first name':
          return fNameIconColor.value
        case 'last name':
          return lNameIconColor.value
        case 'password':
          return passwordEyeIconColor.value
        default:
          return 'primary'
      }
    }

    return {
      ...props,
      showPassword,
      isValidForm,
      isLoadingSignUp,
      errorMessage,
      successMessage,
      passwordHints,
      formInputs,
      getIconColor,
      toggleShowPassword,
      internalGenerateStrongPassword,
      signup,
    }
  },
})
</script>

<style scoped>
.signup-card {
  background: var(--blue-bg);
  overflow: hidden !important;
}

.signup-image {
  width: 350px !important;
  height: 350px !important;
}

.generate-password-span {
  cursor: pointer;
}
</style>
