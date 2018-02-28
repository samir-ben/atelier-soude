
<template> 
<article>
  <h1 class="container" ref="mytitle">{{title}}</h1>
  <p><i>Clique sur réactualiser pour voir les articles</i></p>
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
