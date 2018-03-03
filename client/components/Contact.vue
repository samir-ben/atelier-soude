<template>
<section >
  <div>
    <h1 class="nav-title ">Contacts</h1>
    <b-container>
      <div class="search-bar">
        <input type="text" v-model="search" placeholder="Recherche">
      </div>
    </b-container>
    <button @click="removeButton()" class="bouton-switch d-flex justify-content-center fa fa-list fa-2x" ></button>
    <div v-if="show">
      <div class="container contact-card d-flex justify-content-center ">
        <div class="row ">
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
                      <p class="profile-title"><button class="btn btn-secondary"><a v-bind:href=contact.id> Voir profil</a></button></p>
                      
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
        <th scope="col">Profil</th>
      </tr>
      <transition-group tag="tbody" name="list">
      <tr v-for="contact in filteredContacts" :key="contact.name">  
        <th scope="row" ></th>
          <td><span class="fisrt-letter">{{ contact.firstname }}</span></td>
          <td><span class="fisrt-letter">{{ contact.name }}</span></td>
          <td><span class="fisrt-letter">{{ contact.age }}</span></td>
          <td><span class="fisrt-letter">{{ contact.status }}</span></td>
          <td><span class="fisrt-letter">{{ contact.location }}</span></td>
          <td><span class="fisrt-letter"><button class="btn btn-secondary"><a v-bind:href=contact.id> Voir profil</a></button></span></td>
      </tr>
   </transition-group>
  </table>

</section>
</template>

<script>
import { mapState } from 'vuex'

const contacts = [
  { id: 1, name: 'dupont', firstname: 'xavier', age: '22', status: 'réparateur', location: 'lyon' },
  { id: 2, name: 'moris', firstname: 'boris', age: '26', status: 'adhérent', location: 'lyon' },
  { id: 3, name: 'darq', firstname: 'alexis', age: '33', status: 'réparateur', location: 'lyon' },
  { id: 4, name: 'gislin', firstname: 'david', age: '56', status: 'adhérent', location: 'poncharat' },
  { id: 5, name: 'bensaid', firstname: 'yacine', age: '19', status: 'adhérent', location: 'lyon' },
  { id: 6, name: 'verron', firstname: 'mathilde', age: '20', status: 'réparateur', location: 'lyon' },
  { id: 7, name: 'chatard', firstname: 'clément', age: '27', status: 'adhérent', location: 'lyon' },
  { id: 8, name: 'zola', firstname: 'emile', age: '43', status: 'adhérent', location: 'lyon' },
  { id: 9, name: 'hugo', firstname: 'victor', age: '40', status: 'adhérent', location: 'lyon' },
  { id: 10, name: 'dumortier', firstname: 'lisa', age: '55', status: 'adhérent', location: 'lyon' },
  { id: 11, name: 'roubhi', firstname: 'karim', age: '25', status: 'adhérent', location: 'lyon' },
  { id: 12, name: 'rabhi', firstname: 'smain', age: '25', status: 'adhérent', location: 'tarare' },
  { id: 13, name: 'rabéi', firstname: 'eric', age: '29', status: 'adhérent', location: 'lyon' },
  { id: 14, name: 'donalds', firstname: 'dave', age: '31', status: 'adhérent', location: 'lyon' },
  { id: 15, name: 'carter', firstname: 'shaun', age: '30', status: 'réparateur', location: 'lyon' },
  { id: 16, name: 'bendaoud', firstname: 'samir', age: '24', status: 'adhérent', location: 'tarare' },
  { id: 17, name: 'var', firstname: 'elodie', age: '31', status: 'adhérent', location: 'lyon' },
  { id: 18, name: 'sapin', firstname: 'yohan', age: '45', status: 'adhérent', location: 'lyon' },
  { id: 19, name: 'meunier', firstname: 'patrick', age: '41', status: 'adhérent', location: 'lyon' },
  { id: 20, name: 'abdoulrahim', firstname: 'djamila', age: '37', status: 'adhérent', location: 'tarare' },
  { id: 21, name: 'debourd', firstname: 'charles', age: '26', status: 'adhérent', location: 'lentilly' },
]

export default {
  name: 'Contact',
  computed: {
    ...mapState({
      user: state => state.user,
    }),
    filteredContacts: function(){
      return this.contacts.filter((contact)=>{
        return contact.firstname.toLowerCase().match(this.search.toLowerCase()) || contact.name.toLowerCase().match(this.search.toLowerCase()) || contact.age.toLowerCase().match(this.search.toLowerCase()) || contact.status.toLowerCase().match(this.search.toLowerCase()) || contact.location.toLowerCase().match(this.search.toLowerCase())
      });
    }

  },
  data () {
    return {
      contacts: contacts,
      search: '',
      show: true,
    }
  },
  methods: {
      removeButton: function() {
        if (this.show = !this.show) {
          $( ".bouton-switch" ).removeClass( "fa-list fa-id-card-o" ).addClass( "fa-list" );
        }
        else {
          $( ".bouton-switch" ).removeClass( "fa-list" ).addClass( "fa-id-card-o fa-list" );
        }

       }
  }
}
</script>

<style scoped>
.search-bar input{
  width: 100%;
  padding: 0;
  margin: 10px auto 20px auto;
}
.bouton-switch{
  position: relative;
  margin: 0px auto 15px auto;
  background-color: transparent;
  border: transparent;
  padding: 0;
}
.bouton-switch:hover{
  color: gray;
}
.contact-card  {
display: inline-block !important;
text-align: center;
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
  transition: all 0.2s;
}
.list-enter, .list-leave-to {
  opacity: 0.5;
  transform: translateY(2px);
}
a:link 
{ 
text-decoration:none; 
} 
a {
  color: #FFF;
}



</style>
