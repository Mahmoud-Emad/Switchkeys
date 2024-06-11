<template>
  <v-card class="env-card mt-6">
    <v-card-title>
      <h1 class="env-logo">{{ environment.name }}</h1>
    </v-card-title>

    <v-card-text>
      <div class="mb-4">
        <v-tooltip text="Organization name" location="right" class="hint">
          <template #activator="{ props }">
            <v-chip color="white" class="mr-3 hint" v-bind="props">{{
              environment.project.organization.title
            }}</v-chip>
          </template>
        </v-tooltip>

        <v-tooltip text="Project name" location="right" class="hint">
          <template #activator="{ props }">
            <v-chip color="white" class="mr-3 hint" v-bind="props">{{
              environment.project.title
            }}</v-chip>
          </template>
        </v-tooltip>
      </div>

      <v-divider style="color: gray"></v-divider>

      <div class="mt-4 mb-4">
        <v-row>
          <v-col
            class="d-flex justify-center"
            v-for="btn of actions"
            :key="btn.title"
          >
            <v-tooltip :text="btn.hint" location="bottom" class="hint">
              <template #activator="{ props }">
                <v-btn
                  :color="btn.color"
                  variant="tonal"
                  v-bind="props"
                  @click="btn.click"
                >
                  <v-icon class="mr-1">
                    {{ btn.icon }}
                  </v-icon>
                  {{ btn.title }}
                </v-btn>
              </template>
            </v-tooltip>
          </v-col>
        </v-row>
      </div>

      <v-divider style="color: gray"></v-divider>
    </v-card-text>

    <v-card-actions class="mb-2">
      <v-row>
        <v-col cols="6" class="d-flex justify-start">
          <v-row>
            <v-col cols="12" class="pa-0 ma-0 ml-4 mb-0 env-actions-dates">
              <small class="mr-2">Created at</small>
              <small>{{ environment.createdAt }}</small>
            </v-col>
            <v-col
              cols="12"
              class="pa-0 ma-0 d-flex align-center env-actions-dates"
            >
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

import type { IEnvironment } from '../../utils/types'

export default defineComponent({
  name: 'OrganizationsComponent',
  props: {
    environment: {
      type: Object as PropType<IEnvironment>,
      required: true,
    },
  },

  setup() {
    const router = useRouter()

    const navigateToOrganization = (environment: { id: number }) => {
      router.push(`/environments/${environment.id}`)
    }

    const goToFeats = () => {}
    const goToUsers = () => {}
    const goToSetts = () => {}

    const actions = [
      {
        title: 'Features',
        click: goToFeats,
        icon: 'mdi-rocket-launch',
        color: 'info',
        hint: 'See enviroment features.',
      },
      {
        title: 'Users',
        click: goToUsers,
        icon: 'mdi-account-group',
        color: 'warning',
        hint: 'See enviroment users.',
      },
      {
        title: 'Settings',
        click: goToSetts,
        icon: 'mdi-folder-wrench-outline',
        color: 'green',
        hint: 'Manage enviroment settings.',
      },
    ]

    return {
      actions,
      navigateToOrganization,
    }
  },
})
</script>

<style scoped>
.env-logo {
  color: #7e978aed !important;
}

.env-card:hover :deep(.env-logo) {
  color: #37b976ed !important;
}

.hint {
  cursor: help;
}

.env-actions-dates::before {
  background: #37b976ed;
}

.env-charts::before {
  background: #37b976ed;
}

.env-actions-dates::before,
.env-charts::before {
  content: '';
  width: 5px;
  height: 5px;
  display: inline-flex;
  border-radius: 50%;
  margin-right: 4px;
  align-items: center;
}

.env-actions-dates,
.env-charts {
  margin-left: 20px !important;
  align-items: center !important;
  display: flex;
}
.env-charts {
  margin-left: 0px !important;
}
</style>
