import 'babel-polyfill'
import Vue from 'vue'
import { sync } from 'vuex-router-sync'
import App from './App'
import router from './routes'
import store from './stores/main'
import BootstrapVue from 'bootstrap-vue'
import VueResource from 'vue-resource'
import 'vue-event-calendar/dist/style.css' //^1.1.10, CSS has been extracted as one file, so you can easily update it.
import vueEventCalendar from 'vue-event-calendar'
Vue.use(vueEventCalendar, {locale: 'fr'}) 

Vue.use(VueResource);

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

sync(store, router)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
})
