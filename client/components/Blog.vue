
<template> 
<article>
  <h1 class="container nav-title " ref="mytitle">{{title}}</h1>
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

</style>
