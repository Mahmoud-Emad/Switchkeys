<template>
  <v-card class="env-card mt-6" style="width: 100%">
    <v-card-title>
      <h1 class="env-logo">{{ environment.name }}</h1>
      <v-tooltip text="Organization name" location="bottom" class="hint">
        <template #activator="{ props }">
          <v-chip color="warning" class="mr-3 hint" v-bind="props">{{ environment.project.organization.title }}</v-chip>
        </template>
      </v-tooltip>

      <v-tooltip text="Project name" location="bottom" class="hint">
        <template #activator="{ props }">
          <v-chip color="success" class="mr-3 hint" v-bind="props">{{ environment.project.title }}</v-chip>
        </template>
      </v-tooltip>
    </v-card-title>
    <v-divider></v-divider>
    <v-card-actions>
      <v-row>
        <v-col cols="6" class="d-flex justify-start">
          <v-row>
            <v-col cols="12" class="pa-0 ma-0 ml-4 mb-0 mt-2 org-actions-dates">
              <small class="mr-2">Created at</small>
              <small>{{ environment.createdAt }}</small>
            </v-col>
            <v-col cols="12" class="pa-0 ma-0 ml-4 d-flex align-center mb-3 org-actions-dates">
              <small class="mr-2">Modified at</small>
              <small>{{ environment.modifiedAt }}</small>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="6" class="d-flex justify-end">
          <v-btn
            class="rounded"
            color="white"
            variant="tonal"
            @click="navigateToOrganization(environment)"
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
import type { IEnvironment } from '@/utils/types'

export default defineComponent({
  name: 'OrganizationsComponent',
  props: {
    environment: {
      type: Object as PropType<IEnvironment>,
      required: true
    }
  },

  setup() {
    const router = useRouter()

    const navigateToOrganization = (environment: { id: number }) => {
      router.push(`/environments/${environment.id}`)
    }

    return {
      navigateToOrganization,
    }
  }
})
</script>

<style scoped>
.env-logo {
  color: #7e978aed !important;
}

.env-card:hover :deep(.env-logo) {
  color: #37b976ed !important;
}

.hint{
  cursor: help;
}

.org-actions-dates::before {
  content: '';
  width: 5px;
  height: 5px;
  display: inline-flex;
  background: #eba139;
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
