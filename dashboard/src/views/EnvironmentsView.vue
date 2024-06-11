<template>
  <ComponentTransition>
    <template v-slot:component>
      <EnvironmentsComponent />
    </template>
  </ComponentTransition>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import EnvironmentsComponent from '../components/environments/EnvironmentComponent.vue'
import ComponentTransition from '../components/ui/ComponentTransition.vue'

export default defineComponent({
  nbame: 'DashboardView',
  components: { EnvironmentsComponent, ComponentTransition },
})
</script>
