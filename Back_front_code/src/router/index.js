import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import bpm from '@/components/bpm.vue'
import userlogin from '@/components/user/userlogin.vue'
import userjoin from '@/components/user/userjoin.vue'
import temp from '@/components/temp.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },

  {
    path:'/bpm',
    name: 'bpm',
    component: bpm
  },
 
  {
    path: '/userlogin',
    name: 'userlogin',
    component: userlogin
  },
  {
    path:'/userjoin',
    name:'userjoin',
    component: userjoin
  },
  {
    path :'/temp',
    name:'temp',
    component:temp
  }, 

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
