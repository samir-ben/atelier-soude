import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './components/Home'
import Blog from './components/Blog'
import PersonalPage from './components/PersonalPage'
import Contact from './components/Contact'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    { path: '/home', component: Home, name: 'Home' },
    { path: '/blog', component: Blog, name: 'Blog' },
    { path: '/personal-page', component: PersonalPage, name: 'PersonalPage' },
    { path: '/contact', component: Contact, name: 'Contact' },
  ],
  hashbang: false,
  mode: 'history',
  linkActiveClass: 'active',
})
