<template>
<article>
  <h1 class="container" ref="mytitle">{{title}}</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto, voluptatum, veritatis. Delectus, a, laboriosam! Alias, nobis? Labore, corrupti. Asperiores harum architecto voluptate consequuntur pariatur hic neque possimus deserunt delectus molestias!</p>
</article>
 
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Blog',
  computed: {
    ...mapState({
      user: state => state.user,
    }),
  },
  data () {
    return {
      title: 'Blog'
    }
  },

}
</script>

<style scoped>
h1 {
	margin: 0;
	padding: 0;
}

</style>
