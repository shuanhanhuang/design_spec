import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import studentView from '../views/students/view.vue'
import studentCreate from '../views/students/create.vue'
import studentEdit from '../views/students/Edit.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/students',
      name: 'students',

      component: studentView
    },
    {
      path: '/students/create',
      name: 'studentCreate',
      component: studentCreate
    },
    {
      path: '/students/:id/edit',
      name: 'studentEdit',
      component: studentEdit
    }
  ]
})

export default router
