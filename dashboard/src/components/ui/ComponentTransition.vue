<template>
  <div class="load-component v-container mt-0 pt-0" id="component">
    <slot name="component" />
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'

export default defineComponent({
  nbame: 'ComponentTransition',
  setup() {
    onMounted(() => {
      const component = document.getElementById('component')
      if (component) {
        setTimeout(() => {
          component.style.bottom = `0`
        }, 10)
      }
    })
  },
})
</script>

<style>
.load-component {
  overflow: hidden;
  position: relative;
  bottom: -5%;
  transition: 0.3s;
  margin-top: 0px !important;
  padding-top: 0px !important;
}
</style>
