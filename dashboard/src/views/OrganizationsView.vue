<template>
  <ComponentTransition>
    <template v-slot:component>
      <OrganizationsComponent />
    </template>
  </ComponentTransition>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import OrganizationsComponent from "@/components/organizations/OrganizationsComponent.vue"
import ComponentTransition from "@/components/ui/ComponentTransition.vue";

export default defineComponent({
  nbame: "DashboardView",
  components: {OrganizationsComponent, ComponentTransition},
})
</script>
