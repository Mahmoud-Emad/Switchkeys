<template>
  <v-card class="project-card mt-6">
    <v-card-title>
      <h1 class="project-logo">{{ generateCardLogo(project.title) }}</h1>
      <v-row>
        <v-col>
          <div class="d-flex align-center">
            <v-icon>mdi-lan</v-icon>
            <strong class="ml-2">{{ project.title }}</strong>
          </div>
        </v-col>
        <v-col>
          <v-tooltip location="bottom" width="500">
            <template #default>
              <OrganizationsCard
                :organization="project.organization"
                :no-view="true"
                class="mb-5"
              />
            </template>
            <template #activator="{ props }">
              <div v-bind="props" class="d-flex align-center show-org">
                <v-icon>mdi-domain</v-icon>
                <strong class="ml-2">{{ project.organization.title }}</strong>
              </div>
            </template>
          </v-tooltip>
        </v-col>
      </v-row>
      <v-expansion-panels class="mt-4 mb-4">
        <v-expansion-panel class="project-card" title="Environments">
          <template #text>
            <v-row class="w-100 d-flex justify-space-between" width="100">
              <v-col
                v-for="env of project.environments"
                :key="env.environmentKey"
              >
                <v-chip variant="outlined" :color="env.chipColor">
                  {{ env.name }}
                </v-chip>
              </v-col>
            </v-row>
          </template>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-card-title>
    <v-divider></v-divider>
    <v-card-actions>
      <v-row>
        <v-col cols="6" class="d-flex justify-start">
          <v-row>
            <v-col
              cols="12"
              class="pa-0 ma-0 ml-4 mb-0 mt-2 project-actions-dates"
            >
              <small class="mr-2">Created at</small>
              <small>{{ project.createdAt }}</small>
            </v-col>
            <v-col
              cols="12"
              class="pa-0 ma-0 ml-4 d-flex align-center mb-3 project-actions-dates"
            >
              <small class="mr-2">Modified at</small>
              <small>{{ project.modifiedAt }}</small>
            </v-col>
          </v-row>
        </v-col>
        <v-col cols="6" class="d-flex justify-end">
          <v-btn
            class="rounded"
            color="white"
            variant="tonal"
            @click="navigateToProject(project)"
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

import { generateCardLogo } from '../../utils/generators'
import type { IProject } from '../../utils/types'
import OrganizationsCard from '../organizations/OrganizationsCard.vue'

export default defineComponent({
  name: 'OrganizationsComponent',
  components: {
    OrganizationsCard,
  },
  props: {
    project: {
      type: Object as PropType<IProject>,
      required: true,
    },
  },

  setup() {
    const router = useRouter()

    const navigateToProject = (project: { id: number }) => {
      router.push(`/projects/${project.id}`)
    }

    return {
      navigateToProject,
      generateCardLogo,
    }
  },
})
</script>

<style scoped>
.project-logo {
  color: #698194ed !important;
}

.project-card:hover :deep(.project-logo) {
  color: #376bb9ed !important;
}

.project-actions-dates::before {
  content: '';
  width: 5px;
  height: 5px;
  display: inline-flex;
  background: #eba139;
  border-radius: 50%;
  margin-right: 4px;
  align-items: center;
}

.project-actions-dates {
  margin-left: 20px !important;
  align-items: center !important;
  display: flex;
}

.project-org-card {
  display: none;
}

.show-org {
  cursor: help;
}

.show-org:hover :deep(.project-org-card) {
  display: block !important;
}
</style>
