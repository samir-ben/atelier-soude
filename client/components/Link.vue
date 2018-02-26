<template>
  <div>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laborum magni, at, sapiente consequuntur non est deleniti veritatis quasi nemo, error dolor earum cupiditate iure laboriosam atque possimus id tempora nisi.</p>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Link',
  computed: {
    ...mapState({
      user: state => state.user,
    }),
  },
}
</script>

<style scoped>

</style>
