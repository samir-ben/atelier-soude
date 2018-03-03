import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './components/Home'
import Blog from './components/Blog'
import PersonalPage from './components/PersonalPage'
import Contact from './components/Contact'
import ShowContact from './components/ShowContact'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    { path: '/home', component: Home, name: 'Home' },
    { path: '/blog', component: Blog, name: 'Blog' },
    { path: '/personal-page', component: PersonalPage, name: 'PersonalPage' },
    { path: '/contact', component: Contact, name: 'Contact' },
    { path: '/contact/:id', component: ShowContact, name: 'ShowContact' },
  ],
  hashbang: false,
  mode: 'history',
  linkActiveClass: 'active',
})
