<template> 
<div>
  <p>{{getRange}}</p>
  <div v-if="show">
    <ul >
      <li>{{getFirstname()}}</li>
      <li>{{getName()}}</li>
      <li>{{getAge()}}</li>
      <li>{{getStatus()}}</li>
      <li>{{getLocation()}}</li>
    </ul>
  </div>

  <div v-if="!show">
    <p class="error-message">{{messageError}}</p>
  </div>
  <b-link to="/contact/">Retour</b-link>


</div> 
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
  },
  data () {
    return {
      id: this.$route.params.id,
      contacts: contacts,
      messageError: 'Contact non trouvé',
      show: true,
    }
  },
  // created(){
  //   this.$http.get(contacts + this.id).then(function(data){
  //     this.contacts = data.contacts.name;
  //   });
  // },
  methods: {
    getName(){
      if (this.id <= contacts.length){      
        return contacts[this.id-1].name;
    }  
  },

    getFirstname(){
      if (this.id <= contacts.length){
        return contacts[this.id-1].firstname;
    }    
    },

    getAge(){
      if (this.id <= contacts.length){
        return contacts[this.id-1].age;
    }    
    },

    getStatus(){
      if (this.id <= contacts.length){
        return contacts[this.id-1].status;
    }    
    },

    getLocation(){
      if (this.id <= contacts.length){
        return contacts[this.id-1].location;
      }    
    },
  },
  computed:{
      getRange(){
        if (this.id > contacts.length){
          this.show = !this.show;
        }
        else if (this.id <= 0){
          this.show = !this.show;
        }
        else if ($.isNumeric(this.id) === false){
          this.show = !this.show;
        }
    },
  }

}
</script>

<style scoped>
.error-message{
  background-color: #FEF6F6;
  color: #863430;
  padding: 10px;
  font-size: 1.2em;
  border: 1px solid #DAB6B5;
}

</style>
