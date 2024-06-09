<template>
  <SearchCards :objects="projects" @update:objects="updatefilteredProjects"/>

  <div class="w-100">
    <v-row class="w-100">
      <v-col
        cols="4"
        class="w-100 d-flex justify-space-between"
        v-for="project in filteredProjects"
        :key="project.id"
      >
      <ProjectCard :project />
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import ProjectCard from './ProjectCard.vue';
import type { IProject } from '@/utils/types';
import SearchCards from '@/layoutes/SearchCards.vue';

export default defineComponent({
  name: 'OrganizationsComponent',
  components: {
    ProjectCard,
    SearchCards,
  },

  setup() {
    const projects = [
      {
        id: 1,
        title: 'TFGrid',
        environments: [
        { name: 'development', environmentKey: 'hgas245asdg#$ASDsdsa', chipColor: "orange" },
          { name: 'staging', environmentKey: 'edfss245as#$ASDsdssda', chipColor: "yellow" },
          { name: 'production', environmentKey: 'cshkmgb#$ASDsdssda', chipColor: "success" }
        ],
        createdAt: '19-06-2024',
        modifiedAt: '19-06-2024',
        organization: {
          id: 2,
          title: 'Threefold',
          projects: 105,
          members: 22,
          createdAt: '19-06-2024',
          modifiedAt: '19-06-2024'
        }
      },
      {
        id: 1,
        title: 'StoryMith',
        environments: [
          { name: 'development', environmentKey: 'hgas245asdg#$ASDsdsa', chipColor: "orange" },
          { name: 'staging', environmentKey: 'edfss245as#$ASDsdssda', chipColor: "yellow" },
          { name: 'production', environmentKey: 'cshkmgb#$ASDsdssda', chipColor: "success" }
        ],
        createdAt: '19-06-2024',
        modifiedAt: '19-06-2024',
        organization: {
          id: 1,
          title: 'SwitchKeys',
          projects: 15,
          members: 12,
          createdAt: '19-06-2024',
          modifiedAt: '19-06-2024'
        }
      }
    ]
    const filteredProjects = ref<IProject[]>(projects)
    const updatefilteredProjects = (objs: IProject[]) => filteredProjects.value = objs;


    return {
      projects,
      filteredProjects,
      updatefilteredProjects,
    }
  }
})
</script>
