import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '@/views/DashboardView.vue'
import OrganizationsView from '@/views/OrganizationsView.vue'
import ProjectsView from '@/views/ProjectsView.vue'
import EnvironmentsComponent from '@/views/EnvironmentsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: DashboardView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView
    },
    {
      path: '/organizations',
      name: 'organizations',
      component: OrganizationsView
    },
    {
      path: '/projects',
      name: 'projects',
      component: ProjectsView
    },
    {
      path: '/environments',
      name: 'environments',
      component: EnvironmentsComponent
    }
  ]
})

export default router
