<template>
  <v-card class="org-card mt-6" style="width: 100%">
    <v-card-title>
      <h1 class="org-logo">{{ generateCardLogo(organization.title) }}</h1>
      <div class="d-flex align-center">
        <v-icon>mdi-domain</v-icon>
        <strong class="ml-2">{{ organization.title }}</strong>
      </div>
    </v-card-title>
    <v-card-text>
      <v-chip color="success" variant="tonal">{{ organization.projects }}</v-chip>
      Projects associated, There are
      <v-chip color="yellow" variant="tonal">{{ organization.members }}</v-chip>
      members.
    </v-card-text>
    <v-divider></v-divider>
    <v-card-actions>
      <v-row>
        <v-col cols="6" class="d-flex justify-start">
          <v-row>
            <v-col cols="12" class="pa-0 ma-0 ml-4 mb-0 mt-2 org-actions-dates">
              <small class="mr-2">Created at</small>
              <small>{{ organization.createdAt }}</small>
            </v-col>
            <v-col cols="12" class="pa-0 ma-0 ml-4 d-flex align-center mb-3 org-actions-dates">
              <small class="mr-2">Modified at</small>
              <small>{{ organization.modifiedAt }}</small>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="6" class="d-flex justify-end">
          <v-btn
            v-if="!noView"
            class="rounded"
            color="white"
            variant="tonal"
            @click="navigateToOrganization(organization)"
          >
            View
          </v-btn>
        </v-col>
      </v-row>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts">
import { defineComponent, type PropType } from 'vue'
import { useRouter } from 'vue-router'
import type { IOrganization } from "@/utils/types"
import { generateCardLogo } from '@/utils/generators';

export default defineComponent({
  name: 'OrganizationsCard',
  props: {
    organization: {
      type: Object as PropType<IOrganization>,
      required: true
    },
    noView: {
      type: Boolean,
      required: false,
    },
  },

  setup() {
    const router = useRouter()

    const navigateToOrganization = (organization: { id: number }) => {
      router.push(`/organizations/${organization.id}`)
    }

    return {
      navigateToOrganization,
      generateCardLogo
    }
  }
})
</script>

<style scoped>
.org-logo {
  color: #978d7eed !important;
}

.org-card:hover :deep(.org-logo) {
  color: #b18952 !important;
}

.org-actions-dates::before {
  content: '';
  width: 5px;
  height: 5px;
  display: inline-flex;
  background: #4ddd4d5c;
  border-radius: 50%;
  margin-right: 4px;
  align-items: center;
}

.org-actions-dates {
  margin-left: 20px !important;
  align-items: center !important;
  display: flex;
}
</style>
