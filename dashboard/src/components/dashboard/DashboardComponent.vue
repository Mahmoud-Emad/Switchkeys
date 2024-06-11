<template>
  <router-link width="80%" :to="app.route" v-for="app of apps" :key="app.title">
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
        icon: 'mdi-domain',
        title: 'Organizations',
        iconColor: 'orange',
        route: '/organizations',
        description: 'Manage and view all organizations you own or belong to.',
      },
      {
        icon: 'mdi-lan',
        title: 'Projects',
        iconColor: 'dodgerblue',
        route: '/projects',
        description:
          "Manage and access all projects you're involved with, whether as an owner or member.",
      },
      {
        icon: 'mdi-account-multiple',
        title: 'Members',
        iconColor: 'yellow',
        route: '/members',
        description: 'View and message members in your organizations.',
      },
      {
        icon: 'mdi-sprout',
        title: 'Environments',
        iconColor: 'green',
        route: '/environments',
        description: 'View and manage all accessible environments.',
      },
      {
        icon: 'mdi-account',
        title: 'Account',
        iconColor: 'deepskyblue',
        route: '/account',
        description: 'Manage and update your account.',
      },
      {
        icon: 'mdi-cog',
        title: 'Settings',
        iconColor: 'orange',
        route: '/settings',
        description:
          'Manage personalization, including profile management and other settings.',
      },
    ]
    return {
      apps,
    }
  },
})
</script>
