<template>
  <div class="loading" v-if="isLoading || showSignUpDialog">
    <div v-if="isLoading" class="spinner-container">
      <atom-spinner :animation-duration="1000" :size="60" />
      <strong class="ml-2">{{ loadingMessage }}</strong>
    </div>

    <v-container v-if="showSignUpDialog">
      <sign-up-component
        :open-dialog="showSignUpDialog"
        @update:close-dialog="closeSignUpDialog"
      />
    </v-container>
  </div>
</template>

<script lang="ts">
import { AtomSpinner } from 'epic-spinners'
import { defineComponent, onMounted, onUnmounted, ref, watch } from 'vue'

import SignUpComponent from '../auth/SignUpComponent.vue'

export default defineComponent({
  name: 'HomeComponent',
  components: { AtomSpinner, SignUpComponent },
  props: {
    isLoading: {
      type: Boolean,
      required: true,
    },
  },
  emits: [
    'close:loading',
    'show:loading',
    'show:auth-dialogs',
    'close:auth-dialogs',
  ],

  setup(props, { emit }) {
    const showSignUpDialog = ref(false)
    const loadingMessage = ref<string>('Loading SwitchKeys dashboard')
    const TOKENS_KEY = import.meta.env.VITE_SWITCHKEYS_TOKENS

    const baseMessage = 'Loading SwitchKeys dashboard'
    let interval: NodeJS.Timeout | null = null

    const startLoading = () => {
      // isLoading.value = true;
      let count = 0
      interval = setInterval(() => {
        count = (count % 3) + 1
        loadingMessage.value = baseMessage + '.'.repeat(count)
      }, 1000)
    }

    const stopLoading = () => {
      if (interval) {
        clearInterval(interval)
        interval = null
      }
      emit('close:loading')
      loadingMessage.value = baseMessage
    }

    const closeSignUpDialog = () => {
      showSignUpDialog.value = false
      emit('close:auth-dialogs')
    }

    onMounted(() => {
      startLoading()
      const tokens = localStorage.getItem(TOKENS_KEY)
      if (tokens) {
        // TODO: Validate the access token or use the refresh token to get new one.
        stopLoading() // Remove this if validation logic will keep loading
        emit('close:auth-dialogs')
      } else {
        showSignUpDialog.value = true
        stopLoading()
        emit('show:auth-dialogs')
      }
    })

    onUnmounted(() => {
      // stopLoading();
    })

    watch(
      () => props.isLoading,
      (newVal) => {
        if (!newVal) {
          stopLoading()
        }
      }
    )

    return {
      showSignUpDialog,
      loadingMessage,

      closeSignUpDialog,
    }
  },
})
</script>

<style scoped>
.spinner-container {
  position: fixed;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw;
  /* background-color: rgba(226, 217, 217, 0.253); Optional: Add a semi-transparent background */
  /* z-index: 1000; Ensure it appears above other content */
}
.loading {
  width: 100vw;
  height: 100vh;
  background: rgba(66, 66, 66, 0.774);
  z-index: 1;
}
</style>
