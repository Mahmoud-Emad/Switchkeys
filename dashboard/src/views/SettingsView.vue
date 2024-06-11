<template>
  <ComponentTransition>
    <template v-slot:component>
      <SettingsComponent />
    </template>
  </ComponentTransition>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import SettingsComponent from '../components/settings/SettingsComponent.vue'
import ComponentTransition from '../components/ui/ComponentTransition.vue'

export default defineComponent({
  nbame: 'SettingsView',
  components: { SettingsComponent, ComponentTransition },
})
</script>
