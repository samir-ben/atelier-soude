<template>
<section>
	<div class="profil-card">
  		<b-card title="Card Title"
      		<img src="./static/img/avatar-default.jpg" class="profile-img">
  			<div class="profile-text">
    			<h2 class="profile-name">{{ user.first_name }}</h2>
    			<span class="profile-title">UX / UI Designer</span>
  			</div>
  		</b-card>
	</div>
	<div>
		<b-table striped hover :items="items"></b-table>
	</div>
</section>
</template>

<script>
import { mapState } from 'vuex'

const items = [
  { Date: '12/01/2018', Lieux: 'L\'Atelier Soudé', Objet: 'Réparé', Suivipar: 'Macdonald' },
  { Date: '22/01/2018', Lieux: 'L\'Atelier Soudé', Objet: 'Réparable', Suivipar: 'Shaw' },
  { Date: '01/02/2018', Lieux: 'LAMEC', Objet: 'non réparable', Suivipar: 'Wilson' },
  { Date: '15/02/2018', Lieux: 'L\'Atelier Soudé', Objet: 'autre', Suivipar: 'Carney' }
]

export default {
  name: 'PersonalPage',
  computed: {
    ...mapState({
      user: state => state.user,
    }),
  },
  data () {
    return {
      items: items
    }
  }
}
</script>

<style scoped>
.profil-card {
	width: 170px;
	height: 200px;
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
  font-size: 1.5em;
  text-transform: uppercase;
}
.profile-title {
  color: #999999;
}


</style>
