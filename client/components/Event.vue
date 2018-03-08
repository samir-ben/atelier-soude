<template>
<article>	
  <h1 class="container nav-title">Evénements</h1>
  <table class="table">
  <thead>
    <tr>
      <td><strong>Title</strong></td>
      <td><strong>Message</strong></td>
      <td><strong>Date</strong></td>
      <td><strong>Horaires</strong></td>
      <td><strong>Adresse</strong></td>
      <td></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><input type="text" v-model.prevent="events.addTitle" ></td>
      <td><input type="text" v-model="events.addMessage" ></td>
      <td><input type="date" placeholder="YYYY/MM/DD" required pattern="(?:19|20)[0-9]{2}/(?:(?:0[1-9]|1[0-2])/(?:0[1-9]|1[0-9]|2[0-9])|(?:(?!02)(?:0[1-9]|1[0-2])/(?:30))|(?:(?:0[13578]|1[02])/31))" title="Enter a date in this format YYYY/MM/DD" v-model="events.addDate" ></td>
      <td><input type="text" v-model="events.addSchedule" ></td>
      <td><input type="text" v-model="events.addAddress" ></td>
    </tr>

  </tbody>
      <input type="submit" class="btn" @click.self="addEvent">

</table>
  <vue-event-calendar :events="demoEvents">
      <template scope="props">
        <div v-for="(event, index) in props.showEvents">
          <div class="event-card">
              <h3>{{event.title}}</h3>
              <p>{{event.message}}</p>
              <p>Le {{event.date}}</p>
              <p>{{event.schedule}}</p>
              <p>{{event.address}}</p>
              <button @click="removeEvent(index)">Supprimer</button>
          </div>
        </div>
      </template>
    </vue-event-calendar>
</article>
</template>

<script>
import { mapState } from 'vuex'

const demoEvents = [
  { title: 'Auto-réparation', message:'Chaque mercredi c\'est permanence à la MYNE !', date: '2018/03/11', schedule: 'De 18:00 à 21:00', address: 'La MYNE (1 rue du Luizet, 69100)'},
  { title: 'Auto-réparation', message:'Chaque mercredi c\'est permanence à la MYNE !', date: '2018/03/12', schedule: 'De 18:00 à 21:00', address: 'La MYNE (1 rue du Luizet, 69100)'},
  { title: 'Auto-réparation', message:'Chaque mercredi c\'est permanence à la MYNE !', date: '2018/03/16', schedule: 'De 18:00 à 21:00', address: 'La MYNE (1 rue du Luizet, 69100)'},
  { title: 'Auto-réparation', message:'Chaque mercredi c\'est permanence à la MYNE !', date: '2018/03/22', schedule: 'De 18:00 à 21:00', address: 'La MYNE (1 rue du Luizet, 69100)'},
  { title: 'Auto-réparation', message:'Chaque mercredi c\'est permanence à la MYNE !', date: '2018/03/24', schedule: 'De 18:00 à 21:00', address: 'La MYNE (1 rue du Luizet, 69100)'},
  { title: 'Auto-réparation', message:'Chaque mercredi c\'est permanence à la MYNE !', date: '2018/03/27', schedule: 'De 18:00 à 21:00', address: 'La MYNE (1 rue du Luizet, 69100)'},
  { title: 'Auto-réparation', message:'Chaque mercredi c\'est permanence à la MYNE !', date: '2018/03/30', schedule: 'De 18:00 à 21:00', address: 'La MYNE (1 rue du Luizet, 69100)'},
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
      events :{
        addTitle:'',
        addMessage:'',
        addDate:'',
        addSchedule:'',
        addAddress:'',
      },
      event: []
    }
  },
   methods:{
    addEvent: function(){
      this.demoEvents.push({
        title: this.events.addTitle,
        message: this.events.addMessage,
        date: this.events.addDate,
        schedule: this.events.addSchedule,
        address: this.events.addAddress,
      });
      this.events.addTitle = '';
      this.events.addMessage = '';
      this.events.addDate = '';
      this.events.addSchedule = '';
      this.events.addAddress = '';
    },
    removeEvent: function(index){
      //console.log(row);
       this.demoEvents.splice(index, 1);
    }
  }
}
</script>

<style scoped>
.table{
  margin-bottom: 40px;
}
.event-card{
  background-color: #fff;
  color: black;
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 10px;
}

</style>