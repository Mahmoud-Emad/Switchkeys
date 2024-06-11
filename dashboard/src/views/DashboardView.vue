<template>
  <ComponentTransition>
    <template v-slot:component>
      <DashboardComponent />
    </template>
  </ComponentTransition>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import DashboardComponent from '../components/dashboard/DashboardComponent.vue'
import ComponentTransition from '../components/ui/ComponentTransition.vue'

export default defineComponent({
  nbame: 'DashboardView',
  components: { DashboardComponent, ComponentTransition },
})
</script>
