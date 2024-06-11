<template>
  <SearchCards :objects="environments" @update:objects="updateEnvironments" />

  <div>
    <v-row>
      <v-col
        cols="12"
        md="6"
        sm="12"
        lg="4"
        xl="4"
        v-for="environment in filteredEnvs"
        :key="environment.id"
      >
        <EnvironmentCard :environment />
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

import SearchCards from '../../layoutes/SearchCards.vue'
import type { IEnvironment } from '../../utils/types'
import EnvironmentCard from './EnvironmentCard.vue'

export default defineComponent({
  name: 'OrganizationsComponent',
  components: {
    EnvironmentCard,
    SearchCards,
  },

  setup() {
    const environments: IEnvironment[] = [
      {
        id: 1,
        name: 'Development',
        environmentKey: 'hgas245asdg#$ASDsdsa',
        createdAt: '19-06-2024',
        modifiedAt: '19-06-2024',
        project: {
          id: 1,
          title: 'StoryMith',
          environments: [],
          createdAt: '19-06-2024',
          modifiedAt: '19-06-2024',
          organization: {
            id: 1,
            title: 'SwitchKeys',
            projects: 15,
            members: 12,
            createdAt: '19-06-2024',
            modifiedAt: '19-06-2024',
          },
        },
        users: [
          {
            username: 'Ahmed',
            device: {
              deviceType: 'Android',
              version: 'v1515.42.6',
            },
            features: [
              {
                name: 'debug',
                value: 'true',
              },
            ],
          },
        ],
        features: [
          {
            name: 'debug',
            value: 'false',
          },
        ],
      },
      {
        id: 2,
        name: 'Staging',
        environmentKey: 'hgas245asdg#$ASDsdsa',
        createdAt: '19-06-2024',
        modifiedAt: '19-06-2024',
        project: {
          id: 1,
          title: 'TFGrid',
          environments: [],
          createdAt: '19-06-2024',
          modifiedAt: '19-06-2024',
          organization: {
            id: 1,
            title: 'Threefold',
            projects: 15,
            members: 12,
            createdAt: '19-06-2024',
            modifiedAt: '19-06-2024',
          },
        },
        users: [
          {
            username: 'Ahmed',
            device: {
              deviceType: 'Android',
              version: 'v1515.42.6',
            },
            features: [
              {
                name: 'debug',
                value: 'true',
              },
            ],
          },
        ],
        features: [
          {
            name: 'debug',
            value: 'false',
          },
        ],
      },
      {
        id: 3,
        name: 'Production',
        environmentKey: 'hgas245asdg#$ASDsdsa',
        createdAt: '19-06-2024',
        modifiedAt: '19-06-2024',
        project: {
          id: 1,
          title: 'TFGrid',
          environments: [],
          createdAt: '19-06-2024',
          modifiedAt: '19-06-2024',
          organization: {
            id: 1,
            title: 'Threefold',
            projects: 15,
            members: 12,
            createdAt: '19-06-2024',
            modifiedAt: '19-06-2024',
          },
        },
        users: [
          {
            username: 'Ahmed',
            device: {
              deviceType: 'Android',
              version: 'v1515.42.6',
            },
            features: [
              {
                name: 'debug',
                value: 'true',
              },
            ],
          },
        ],
        features: [
          {
            name: 'debug',
            value: 'false',
          },
        ],
      },
    ]
    const filteredEnvs = ref<IEnvironment[]>(environments)

    const updateEnvironments = (objs: IEnvironment[]) =>
      (filteredEnvs.value = objs)

    return {
      environments,
      filteredEnvs,
      updateEnvironments,
    }
  },
})
</script>

<style scoped>
.org-logo {
  color: #7e978aed !important;
}

.org-card:hover :deep(.org-logo) {
  color: #37b976ed !important;
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
