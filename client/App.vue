<template>
<div id="app">
  <top-bar/>
  <div class="container">
    <transition name="bounce" mode="out-in"><router-view></router-view></transition>
  </div>
</div>
</template>

<script>
import TopBar from './components/layout/TopBar'

export default {
  name: 'App',
  components: {
    TopBar,
  },
}
</script>

<style>
body {
    background-color: #F4F3F0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.bounce-enter-active {
  animation: bounce-in .5s;
}
.bounce-leave-active {
  animation: bounce-in .2s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1);
  }
  100% {
    transform: scale(1);
  }
}
</style>
