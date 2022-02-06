import { createRouter, createWebHistory } from 'vue-router'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  /* User */
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('../views/user/SignUp.vue')
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: () => import('../views/user/LogIn.vue')
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: () => import('../views/user/MyAccount.vue')
  },
  /* Courses */
  {
    path: '/courses',
    name: 'Courses',
    component: () => import('../views/courses/Courses.vue')
  },
  {
    path: `/courses/:slug`,
    name: 'Course',
    component: () => import('../views/courses/Course.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
