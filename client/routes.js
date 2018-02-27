

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './components/Home'
import Blog from './components/Blog'
import PersonalPage from './components/PersonalPage'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    { path: '/home', component: Home, name: 'Home' },
    { path: '/blog', component: Blog, name: 'Blog' },
    { path: '/personal-page', component: PersonalPage, name: 'PersonalPage' },
  ],
  hashbang: false,
  mode: 'history',
  linkActiveClass: 'active',
})