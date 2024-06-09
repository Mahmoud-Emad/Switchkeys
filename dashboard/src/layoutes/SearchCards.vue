<template>
  <v-expansion-panels class="mt-6 mb-1" style="width: 99%;" v-model="panel">
    <v-expansion-panel class="project-card">
      <template #title>
        <div v-if="instanceOfIOrganization($props.objects[0])">
          Search by <strong class="ml-1">Organization</strong> name.
        </div>
        <div v-else-if="instanceOfIProject($props.objects[0])">
          Search by <strong class="ml-1">Project</strong> and <strong class="ml-1">Organization</strong> name.
        </div>
        <div v-else-if="instanceOfIEnvironment($props.objects[0])">
          Search by <strong class="ml-1">Environment</strong>, <strong class="ml-1">Project</strong>, and <strong class="ml-1">Organization</strong> name.
        </div>
      </template>
      <template #text>
        <div class="w-100 d-flex justify-center">
          <v-text-field 
            v-model="search" 
            label="Search" 
            variant="underlined" 
            color="white" 
            class="search-field">
          </v-text-field>
        </div>
      </template>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<script lang="ts">
import { defineComponent, ref, watch, type PropType } from 'vue';
import { debounce } from 'lodash-es';
import type { IEnvironment, IOrganization, IProject } from '@/utils/types';

export default defineComponent({
  name: "SearchCards",
  emits: ["update:objects"],
  props: {
    objects: {
      type: Array as PropType<IProject[] | IOrganization[] | IEnvironment[]>,
      required: true,
    }
  },
  setup(props, { emit }) {
    const search = ref<string>('');
    const filteredObjects = ref([...props.objects]);
    const panel = ref([0])

    const instanceOfIProject = (object: any): object is IProject => 'organization' in object;
    const instanceOfIOrganization = (object: any): object is IOrganization => 'projects' in object;
    const instanceOfIEnvironment = (object: any): object is IEnvironment => 'users' in object;

    const performSearch = (query: string) => {
      if (!query) {
        filteredObjects.value = [...props.objects];
        emit("update:objects", filteredObjects.value);
        return;
      }

      const searchLowerCase = query.toLowerCase();

      if (instanceOfIProject(props.objects[0])) {
        filteredObjects.value = (props.objects as IProject[]).filter(obj =>
          obj.title.toLowerCase().includes(searchLowerCase) ||
          obj.organization.title.toLowerCase().includes(searchLowerCase)
        );
      } else if (instanceOfIOrganization(props.objects[0])) {
        filteredObjects.value = (props.objects as IOrganization[]).filter(obj =>
          obj.title.toLowerCase().includes(searchLowerCase)
        );
      } else if (instanceOfIEnvironment(props.objects[0])) {
        filteredObjects.value = (props.objects as IEnvironment[]).filter(obj =>
          obj.name.toLowerCase().includes(searchLowerCase) ||
          obj.project.title.toLowerCase().includes(searchLowerCase) ||
          obj.project.organization.title.toLowerCase().includes(searchLowerCase)
        );
      }
      emit("update:objects", filteredObjects.value);
    };

    const debouncedSearch = debounce(performSearch, 300);

    watch(search, newVal => {
      debouncedSearch(newVal);
    });

    return {
      search,
      panel,

      instanceOfIOrganization,
      instanceOfIProject,
      instanceOfIEnvironment,
    };
  }
});
</script>
