<template>
<article>
  <h1 class="container nav-title ">Accueil</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto, voluptatum, veritatis. Delectus, a, laboriosam! Alias, nobis? Labore, corrupti. Asperiores harum architecto voluptate consequuntur pariatur hic neque possimus deserunt delectus molestias!</p>
</article>
 
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Home',
  computed: {
    ...mapState({
      user: state => state.user,
    }),
  },
}
</script>

<style scoped>

</style>
