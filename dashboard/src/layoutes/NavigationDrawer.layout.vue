<template>
  <v-app>
    <DashboardLoading
      :is-loading="isLoading"
      @show:loading="isLoading = true"
      @show:auth-dialogs="isShowAuthDialog = true"
      @close:loading="isLoading = false"
      @close:auth-dialogs="
        () => {
          isLoading = false
          isShowAuthDialog = false
        }
      "
    />

    <v-navigation-drawer
      app
      class="navigation-drawer-custom"
      :style="{ zIndex: isLoading || isShowAuthDialog ? '0' : '904' }"
    >
      <v-list-item class="mt-4">
        <div class="d-flex align-center">
          <v-img
            src="https://randomuser.me/api/portraits/men/85.jpg"
            class="avatar-img"
          />
          <p class="ml-2">
            Mahmoud Emad
            <small>Owner</small>
          </p>
        </div>
      </v-list-item>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item>
          <v-text-field
            class="search-input mt-2"
            v-model="findSetting"
            variant="underlined"
            label="Find a setting."
            prepend-inner-icon="mdi-magnify"
          />
        </v-list-item>

        <v-list-item
          v-for="tab in filteredTabs"
          :key="tab.id"
          :title="tab.title"
          :value="tab.value"
          :to="tab.route"
          class="text-white"
          @click="activeTab = tab"
          :active="activeTab && activeTab.id === tab.id"
          link
        >
          <template #prepend>
            <v-icon
              :style="{
                marginRight: '-20px',
                color: tab.iconColor,
              }"
              >{{ tab.icon }}</v-icon
            >
          </template>
        </v-list-item>
      </v-list>
      <template v-slot:append>
        <div class="pa-2 mb-3">
          <v-btn block variant="tonal" color="primary" @click="logout">
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    <v-main>
      <v-container class="mt-5">
        <div v-if="activeTab">
          <div class="d-flex align-center">
            <v-tooltip v-if="prevRoute.length > 1">
              <template #default>
                <p>Back to the {{ prevRoute[0] }} page?</p>
              </template>
              <template #activator="{ props }">
                <v-icon
                  v-bind="props"
                  color="white"
                  class="mr-1"
                  size="35"
                  style="cursor: pointer"
                  @Click="() => router.push(`/${prevRoute[0]}`)"
                >
                  mdi-arrow-left
                </v-icon>
              </template>
            </v-tooltip>
            <h2>
              <strong>{{ activeTab.title }}</strong>
            </h2>
          </div>
        </div>
      </v-container>

      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { debounce } from 'lodash-es'
import { defineComponent, onMounted, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import DashboardLoading from '../components/ui/DashboardLoading.vue'

type TabType = {
  id: number
  icon: string
  title: string
  value: string
  iconColor: string
  route: string
}

export default defineComponent({
  name: 'AppBarLayout',
  components: { DashboardLoading },
  setup() {
    const isLoading = ref(true)
    const isShowAuthDialog = ref(true)
    const findSetting = ref<string>('')
    const router = useRouter()
    const route = useRoute()
    const TOKENS_KEY = import.meta.env.VITE_SWITCHKEYS_TOKENS

    const tabs: TabType[] = [
      {
        id: 1,
        icon: 'mdi-view-dashboard',
        title: 'Dashboard',
        value: 'dashboard',
        iconColor: 'deepskyblue',
        route: '/dashboard',
      },
      {
        id: 2,
        icon: 'mdi-domain',
        title: 'Organizations',
        value: 'organizations',
        iconColor: 'orange',
        route: '/organizations',
      },
      {
        id: 3,
        icon: 'mdi-lan',
        title: 'Projects',
        value: 'projects',
        iconColor: 'dodgerblue',
        route: '/projects',
      },
      // {
      //   id: 4,
      //   icon: 'mdi-account-multiple',
      //   title: 'Members',
      //   value: 'members',
      //   iconColor: 'yellow',
      //   route: '/members'
      // },
      {
        id: 5,
        icon: 'mdi-sprout',
        title: 'Environments',
        value: 'environments',
        iconColor: 'green',
        route: '/environments',
      },
      {
        id: 6,
        icon: 'mdi-account',
        title: 'Account',
        value: 'account',
        iconColor: 'deepskyblue',
        route: '/account',
      },
      {
        id: 7,
        icon: 'mdi-cog',
        title: 'Settings',
        value: 'settings',
        iconColor: 'orange',
        route: '/settings',
      },
    ]

    const filteredTabs = ref<TabType[]>(tabs)
    const activeTab = ref<TabType>()

    onMounted(() => {
      isLoading.value = true
      const pathname = window.location.pathname
      const matchedTab = tabs.find((tab) => tab.route === pathname)
      if (matchedTab) {
        activeTab.value = matchedTab
      } else {
        activeTab.value = tabs[0]
        router.push(tabs[0].route)
      }
    })

    const performSearch = (query: string) => {
      if (query) {
        filteredTabs.value = tabs.filter((tab) =>
          tab.title.toLowerCase().includes(query.toLowerCase())
        )
      } else {
        filteredTabs.value = tabs
      }
    }

    const debouncedSearch = debounce(performSearch, 300)

    watch(findSetting, (newVal) => {
      debouncedSearch(newVal)
    })

    watch(
      () => router.currentRoute.value.path,
      (newPath) => {
        const matchedTab = tabs.find((tab) => tab.route === newPath)
        if (matchedTab) {
          activeTab.value = matchedTab
        }
      }
    )

    const logout = () => {
      localStorage.removeItem(TOKENS_KEY)
      window.location.reload()
    }

    const prevRoute = ref<string[]>([])

    watch(route, () => {
      prevRoute.value = route.path.split('/').filter((r) => r.length > 0)
    })

    return {
      isLoading,
      isShowAuthDialog,
      findSetting,
      activeTab,
      filteredTabs,
      prevRoute,
      router,

      logout,
    }
  },
})
</script>

<style scoped>
.avatar-img {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  padding: 10px;
}
.search-input {
  color: white;
  border-color: red !important;
}
</style>
