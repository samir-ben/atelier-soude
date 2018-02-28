<template>
<section >
  <div>
    <b-container>
      <div class="search-bar">
        <input type="text" v-model="search" placeholder="Recherche">
      </div>
    </b-container>
    <i @click="show = !show" class="bouton-switch d-flex justify-content-center fa fa-id-card-o fa-2x" ></i><i @click="show = !show" class="bouton-switch d-flex justify-content-center fa fa-list fa-2x"></i>
    <div v-if="show">
      <div class="container contact-card ">
        <div class="row d-flex justify-content-center">
           <transition-group name="list" tag="p">
              <div v-for="contact in filteredContacts" v-bind:key="contact" class="profil-card list-item" >
                <div class="col-xl-12" >
                <div title="Card Title">
                      <img src="./static/img/avatar-default.jpg" class="profile-img">
                    <div class="profile-text">
                      <h2 class="profile-name"><span class="fisrt-letter">{{contact.firstname}}</span> <span class="fisrt-letter"> {{contact.name}}</span></h2>
                      <p class="profile-title">Age: {{contact.age}}</p>
                      <p class="profile-title">Statut: <span class="fisrt-letter">{{contact.status}}</span></p>
                      <p class="profile-title">Ville: <span class="fisrt-letter">{{contact.location}}</span></p>
                      <button class="btn primary">Voir profil</button>
                    </div>
                  </div>
                </div>
              </div>
            </transition-group>
        </div>
      </div>     
    </div>
  </div>

  <table v-if="!show" class="table table-striped">
      <tr>
        <th scope="col">#</th>
        <th scope="col">Prénom</th>
        <th scope="col">Nom</th>
        <th scope="col">Âge</th>
        <th scope="col">Statut</th>
        <th scope="col">Ville</th>
      </tr>
      <transition-group tag="tbody" name="list">
      <tr v-for="contact in filteredContacts" :key="contact.name">  
        <th scope="row" ></th>
          <td><span class="fisrt-letter">{{ contact.firstname }}</span></td>
          <td><span class="fisrt-letter">{{ contact.name }}</span></td>
          <td><span class="fisrt-letter">{{ contact.age }}</span></td>
          <td><span class="fisrt-letter">{{ contact.status }}</span></td>
          <td><span class="fisrt-letter">{{ contact.location }}</span></td>
      </tr>
   </transition-group>
  </table>

</section>
</template>

<script>
import { mapState } from 'vuex'

const contacts = [
  { name: 'dupont', firstname: 'xavier', age: '22', status: 'réparateur', location: 'lyon' },
  { name: 'moris', firstname: 'boris', age: '26', status: 'adhérent', location: 'lyon' },
  { name: 'darq', firstname: 'alexis', age: '33', status: 'réparateur', location: 'lyon' },
  { name: 'gislin', firstname: 'david', age: '56', status: 'adhérent', location: 'poncharat' },
  { name: 'bensaid', firstname: 'yacine', age: '19', status: 'adhérent', location: 'lyon' },
  { name: 'verron', firstname: 'mathilde', age: '20', status: 'réparateur', location: 'lyon' },
  { name: 'chatard', firstname: 'clément', age: '27', status: 'adhérent', location: 'lyon' },
  { name: 'zola', firstname: 'emile', age: '43', status: 'adhérent', location: 'lyon' },
  { name: 'hugo', firstname: 'victor', age: '40', status: 'adhérent', location: 'lyon' },
  { name: 'dumortier', firstname: 'lisa', age: '55', status: 'adhérent', location: 'lyon' },
  { name: 'roubhi', firstname: 'karim', age: '25', status: 'adhérent', location: 'lyon' },
  { name: 'rabhi', firstname: 'smain', age: '25', status: 'adhérent', location: 'tarare' },
  { name: 'rabéi', firstname: 'eric', age: '29', status: 'adhérent', location: 'lyon' },
  { name: 'donalds', firstname: 'dave', age: '31', status: 'adhérent', location: 'lyon' },
  { name: 'carter', firstname: 'shaun', age: '30', status: 'réparateur', location: 'lyon' },
  { name: 'bendaoud', firstname: 'samir', age: '24', status: 'adhérent', location: 'tarare' },
  { name: 'var', firstname: 'elodie', age: '31', status: 'adhérent', location: 'lyon' },
  { name: 'sapin', firstname: 'yohan', age: '45', status: 'adhérent', location: 'lyon' },
  { name: 'meunier', firstname: 'patrick', age: '41', status: 'adhérent', location: 'lyon' },
  { name: 'abdoulrahim', firstname: 'djamila', age: '37', status: 'adhérent', location: 'tarare' },
  { name: 'debourd', firstname: 'charles', age: '26', status: 'adhérent', location: 'lentilly' },
]

export default {
  name: 'Contact',
  computed: {
    ...mapState({
      user: state => state.user,
    }),
    filteredContacts: function(){

      return this.contacts.filter((contact)=>{
        return contact.firstname.match(this.search) || contact.name.match(this.search)
      });
    }

  },
  data () {
    return {
      contacts: contacts,
      search: '',
      show: true,
    }
  }
}
</script>

<style scoped>
.search-bar input{
  width: 100%;
  margin: 10px 20px 20px 20px;
}
.bouton-switch{
  margin: 0px auto 15px auto;
}
.bouton-switch:hover{
  color: gray;
}
.contact-card{
  float: none;
  margin: 0 auto;
  padding: 0;

}
.profil-card {
	width: 190px;
	height: 300px;
	text-align: center;
}
.profile-img {
  width: 80px;
  display: block;
  height: 7em;
  margin-right: auto;
  margin-left: auto;
  border: .5em solid #f2f2f2;
  border-radius: 100%;
  box-shadow:  0 1px 0 0 rgba(0,0,0,.1);
}
.profile-text {
  margin-top: -3.5em;
  padding: 5em 1.5em 1.5em 1.5em; 
  background: white;
  border-radius: 3px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1)
}
.profile-name{
  margin-right: -1em;
  margin-bottom: .75em;
  margin-left: -1em;
  border-bottom: 1px solid rgba(0,0,0,0.1);
  padding-bottom: .75em;
  font-size: 1.3em;
}
.fisrt-letter{
    display: inline-block;
}
.fisrt-letter:first-letter {
    text-transform: uppercase;
}
.profile-title {
  color: #999999;
}
.list-item {
  display: inline-block;
  margin-right: 10px;
}
.list-enter-active, .list-leave-active {
  transition: all 1s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}

</style>
