<template>
  <router-link :to="app.route" v-for="app of apps" :key="app.title">
    <v-card class="mt-5 app-card">
      <v-card-text>
        <v-row>
          <v-col cols="11" class="d-flex align-center">
            <v-icon :style="{ color: app.iconColor }">{{ app.icon }}</v-icon>
            <div class="">
              <h3 class="ml-2">
                <strong>
                  {{ app.title }}
                </strong>
              </h3>
              <small class="ml-2">{{ app.description }}</small>
            </div>
          </v-col>
          <v-col cols="1" class="d-flex justify-end align-center">
            <v-icon>mdi-chevron-right</v-icon>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </router-link>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import type { DashboardAppType } from '../../utils/types'

export default defineComponent({
  name: 'DashboardComponent',
  setup() {
    const apps: DashboardAppType[] = [
      {
        icon: 'mdi-brush',
        title: 'Themes',
        iconColor: 'white',
        route: '/settings/theme',
        description: 'Customize, create, and manage themes.',
      },
      {
        icon: 'mdi-cloud-key',
        title: 'Accessibility',
        iconColor: 'white',
        route: '/settings/accessibility',
        description:
          'Manage the accessibility of each member registered on all of your organizations.',
      },
    ]
    return {
      apps,
    }
  },
})
</script>
