<template>
<article>	
  <h1 class="container nav-title">Evénements</h1>
  <vue-event-calendar :events="demoEvents" @dayChanged="handleDayChange" class="mt-5"></vue-event-calendar>
</article>
</template>

<script>
import { mapState } from 'vuex'

const demoEvents = [
  { date: '2018/03/15', title:'Atelier réparation', desc: 'Lieux : La Myne à 16h30', customClass: 'disabled highlight', },
  { date: '2018/03/11', title:'Atelier réparation', desc: 'Lieux : MEC à 17h30', customClass: 'disabled highlight' },
  { date: '2018/03/22', title:'Atelier réparation', desc: 'Lieux : La Myne à 16h30', customClass: 'disabled highlight' },
  { date: '2018/03/23', title:'Atelier réparation', desc: 'Lieux : MEC à 17h30', customClass: 'disabled highlight' },
  { date: '2018/03/26', title:'Atelier réparation', desc: 'Lieux : La Myne à 16h30', customClass: 'disabled highlight' },
  { date: '2018/03/30', title:'Atelier réparation', desc: 'Lieux : La Myne à 16h30', customClass: 'disabled highlight' },
]

export default {
  name: 'Event',
  computed: {
    ...mapState({
      user: state => state.user,
    }),
  },
  data () {
    return {
      demoEvents: demoEvents,
    }
  }
}
</script>

<style scoped>

</style>