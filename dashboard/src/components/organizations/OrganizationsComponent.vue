<template>
  <SearchCards :objects="organizations" @update:objects="updateFilteredOrganizations"/>
  <div class="w-100">
    <v-row class="w-100">
      <v-col
        cols="4"
        class="w-100 d-flex justify-space-between"
        v-for="organization in filteredOrganizations"
        :key="organization.id"
      >
      <OrganizationsCard :organization />
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import OrganizationsCard from "./OrganizationsCard.vue";
import SearchCards from '@/layoutes/SearchCards.vue';
import type { IOrganization } from '@/utils/types';

export default defineComponent({
  name: 'OrganizationsComponent',
  components: {
    OrganizationsCard,
    SearchCards
  },

  setup() {
    const organizations = [
      {
        id: 1,
        title: 'SwitchKeys',
        projects: 15,
        members: 12,
        createdAt: '19-06-2024',
        modifiedAt: '19-06-2024'
      },
      {
        id: 2,
        title: 'Threefold',
        projects: 105,
        members: 22,
        createdAt: '19-06-2024',
        modifiedAt: '19-06-2024'
      },
      {
        id: 3,
        title: 'Sonono GmbH',
        projects: 105,
        members: 22,
        createdAt: '19-06-2024',
        modifiedAt: '19-06-2024'
      }
    ];

    const filteredOrganizations = ref<IOrganization[]>(organizations)
    const updateFilteredOrganizations = (objs: IOrganization[]) => filteredOrganizations.value = objs;


    return {
      organizations,
      filteredOrganizations,
      updateFilteredOrganizations
    };
  }
});
</script>
