<template>
  <ComponentTransition>
    <template v-slot:component>
      <ProjectsComponent />
    </template>
  </ComponentTransition>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ProjectsComponent from "@/components/projects/ProjectComponent.vue"
import ComponentTransition from "@/components/ui/ComponentTransition.vue";

export default defineComponent({
  nbame: "DashboardView",
  components: {ProjectsComponent, ComponentTransition},
})
</script>
