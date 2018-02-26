import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './components/Home'
import Link from './components/Link'
import PersonalPage from './components/PersonalPage'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    { path: '/', component: Home, name: 'Home' },
    { path: '/home', component: Home, name: 'Home' },
    { path: '/link', component: Link, name: 'Link' },
    { path: '/personal-page', component: PersonalPage, name: 'PersonalPage' },
  ],
  hashbang: false,
  mode: 'history',
  linkActiveClass: 'active',
})
