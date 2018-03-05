<template>
<header>
<div class="nav-side-menu">
    <div class="brand"><b-link to="/home"><img src="../static/img/logo-atelier-soude.png" width="30"></b-link></div>
    <i class="fa fa-bars fa-2x toggle-btn" data-toggle="collapse" data-target="#menu-content"></i>
        <div class="menu-list">
            <ul id="menu-content" class="menu-content collapse out">
                <li>
                  <b-link to="/home"><i class="fa fa fa-home fa-lg fa-fw sidebar-icon"></i>&nbsp;&nbsp;&nbsp;&nbsp; Accueil</b-link>
                </li>

                <li>
                  <a href="/blog/"><i class="fa fa-newspaper-o fa-lg fa-fw sidebar-icon"></i>&nbsp;&nbsp;&nbsp;&nbsp; Actualités</a>
                </li>
                
                <li>
                  <b-link to="/event"><i class="fa fa-calendar fa-lg fa-fw sidebar-icon"></i>&nbsp;&nbsp;&nbsp;&nbsp; Réservations ateliers</b-link>
                </li>

                 <li>
                  <b-link to="/personal-page"><i class="fa fa-user fa-lg fa-fw sidebar-icon"></i>&nbsp;&nbsp;&nbsp;&nbsp; Espace personnel</b-link>
                </li>
                
                <li>
                  <b-link to="/contact/"><i class="fa fa-users fa-lg fa-fw sidebar-icon"></i>&nbsp;&nbsp;&nbsp;&nbsp; Communauté</b-link>
                </li>
          
                <li  data-toggle="collapse" data-target="#maintenance" class="collapsed">
                    <a href="#"><i class="fa fa-question-circle-o fa-lg fa-fw sidebar-icon"></i>&nbsp;&nbsp;&nbsp;&nbsp; Aide <span class="arrow"></span></a>
                </li>
                <ul class="sub-menu collapse" id="maintenance">
                    <li><a href="#"><i class="fa fa-angle-double-right"></i> Documentations</a></li>
                    <li><a href="#"><i class="fa fa-angle-double-right"></i> Tutoriaux</a></li>
                    <li><a href="#"><i class="fa fa-angle-double-right"></i> Questions</a></li>
                </ul>

                <li>
                  <a href="#"><i class="fa fa-map-signs fa-lg fa-fw sidebar-icon"></i>&nbsp;&nbsp;&nbsp;&nbsp; Lieux</a>
                </li>
            </ul>
     </div>
</div>
<div class="container top-bar">
  <nav class="navbar ">
    <div class="navbar-brand page-title" >{{getTitle()}}</div>
    <div class="navbar-brand name-asso " >L'Atelier Soudé</div>
    <div class="navbar-brand user-name">{{ user.first_name }}</div>
    <div class="navbar-brand login " ><b-link to="/personal-page"><i class="fa fa-user-circle-o fa-2x"></i></b-link></div>
    <div class="navbar-brand arrow-login ">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class=""></i></a>
        <div class="dropdown-menu " aria-labelledby="navbarDropdownMenuLink">
          <a class="dropdown-item" href="#">Mon profil</a>
          <a class="dropdown-item" href="#">Mes cotisations</a>
          <a class="dropdown-item" href="#">Mon suivi de réparation</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Paramètres</a>
          <a class="dropdown-item" href="#">Déconnexion</a>
        </div>
    </div>
  </nav>
</div>
  <hr>
</header>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import Blog from '../Blog'

export default {
  name: 'TopBar',
  components: { 'blog': Blog },
  computed: {
    ...mapState({
      user: state => state.user,
    }),
  },
   data () {
    return {
      title: ''
    }
  },
  methods: {
    ...mapActions([
      'getCurrentUser',
    ]),
    getTitle() {
      // return this.title = $("h1");
      var i = $( "h1" );
      console.log(i);
    }
  },
  mounted () {
    this.getCurrentUser()
  },
}
</script>

<style scoped>
.top-bar {
 width: 100%;
 height: 40px;
}
.page-title {
  position: absolute;
  left: 0;
  margin: 4px 0 0 0;
  padding: 0;
  vertical-align: middle;
  font-size: 1.5em;
}
.name-asso {
  text-align: center;
  margin: 4px 0 0 0;
  font-size: 2em;
  padding: 0;
}
.user-name {
   position: absolute;
   margin: 6px 0 0 0;
  right: 60px;
  padding: 0;
}
.login {
  position: absolute;
  right: 20px;
  margin: 4px 0 0 0;
  padding: 0;
}
.arrow-login {
  position: absolute;
  right: -10px;
  margin: 1px 0 0 0;
  padding: 0;
}
.dropdown-menu  {
    position: absolute;
    top: 20;
    left: -80px;
  }
.brand {
  border-bottom: 0.5px solid #a8a8a8;
}
.fa-user-circle-o, .dropdown-toggle {
  margin-top: 0px;
  text-decoration: none;
  color: #A9A9A9;
}
.dropdown-toggle {
  font-size: 1.5em;
}
.fa-user-circle-o:hover, .dropdown-toggle:hover {
  text-decoration: none;
  color: #212120;
}
.nav-side-menu:hover {
  width: 180px;
}
.main {
    margin-left: 220px;
    padding: 15px;
}
.nav-side-menu {
  overflow: auto;
  background-color: #212120;
  position: fixed;
  top: 0px;
  width: 40px;
  height: 100%;
  color: #e1ffff;
  transition: width .15s;
  z-index: 1;
}
.nav-side-menu .brand {
  background-color: #212120;
  line-height: 50px;
  display: block;
  text-align: center;
  font-size: 14px;
}
.nav-side-menu .toggle-btn {
  display: none;
}
.nav-side-menu ul,
.nav-side-menu li {
  list-style: none;
  padding: 0px;
  margin: 0px;
  line-height: 4rem;
  cursor: pointer;
  visibility: visible !important;
  white-space:nowrap;
}
/*
    .collapsed{
       .arrow:before{
                 font-family: FontAwesome;
                 content: "\f053";
                 display: inline-block;
                 padding-left:10px;
                 padding-right: 10px;
                 vertical-align: middle;
                 float:right;
            }
     }
*/
.nav-side-menu ul :not(collapsed) .arrow:before,
.nav-side-menu li :not(collapsed) .arrow:before {
  font-family: FontAwesome;
  content: "\f078";
  display: inline-block;
  padding-left: 10px;
  padding-right: 10px;
  vertical-align: middle;
  white-space:nowrap;
}
.nav-side-menu li i.sidebar-icon {
    margin-right: 0.6rem;
    font-size: 1.5em;
}
.nav-side-menu ul .active,
.nav-side-menu li .active {
  border-left: 3px solid #e1ffff;
  background-color: #FFFFFF;
}
.nav-side-menu li {
  padding-left: 0px;

  border-bottom: 1px solid #23282e;
}
.nav-side-menu li a {
  display: block;
  text-decoration: none;
  color: #C8C8C8;
}
.nav-side-menu li a i {
  padding-left: 10px;
  width: 20px;
  padding-right: 20px;
}
.nav-side-menu li:hover {
  border-left: 3px solid #e1ffff;
  background-color: #62B587;
  opacity: 0.3;

  -webkit-transition: all .6s ease;
  -moz-transition: all .6s ease;
  -o-transition: all .6s ease;
  -ms-transition: all .6s ease;
  transition: all .6s ease;
}
.nav-side-menu li a:hover {
    color: #FFFFFF;
}
.nav-side-menu ul .sub-menu li.active,
.nav-side-menu li .sub-menu li.active {
  background-color: #FFFFFF;
}
.nav-side-menu ul .sub-menu li,
.nav-side-menu li .sub-menu li {
  background-color: #262625;
  border: none;
  line-height: 3.4rem;
  border-bottom: 1px solid #23282e;
  margin-left: 0px;
}
.nav-side-menu ul .sub-menu li:hover,
.nav-side-menu li .sub-menu li:hover {
  background-color: #FFFFFF;
 
}
.nav-side-menu li .sub-menu li a,
.nav-side-menu ul .sub-menu li a{
    display: block;
    padding-left: 20px;
}
.nav-side-menu ul .sub-menu li a i,
.nav-side-menu li .sub-menu li a i{
    padding-right: 10px !important;
}
@media (max-width: 767px) {
    .main {
        margin-left: 0 !important;
        padding: 0 15px 15px 15px;
    }
  .nav-side-menu {
    position: relative;
    width: 100%;
    margin-bottom: 10px;
  }
  .nav-side-menu .toggle-btn {
    display: block;
    cursor: pointer;
    position: absolute;
    right: 10px;
    top: 9px;
    z-index: 10 !important;
    padding: 3px;
    width: 40px;
    text-align: center;
    background-color: #2e353d;
    color: #FFFFFF;
    border-radius: 4px;
  }
  .brand {
    text-align: left !important;
    font-size: 22px;
    padding-left: 20px;
    line-height: 50px !important;
  }
  .nav-side-menu:hover {
  width: 100%;
  }
}
@media (min-width: 767px) {
  .nav-side-menu .menu-list .menu-content {
    display: block;
  }
}
  @media all and (max-width: 900px)
{
  .dropdown-menu  {
    position: absolute;
    top: 20;
    left: -110px;
  }
}
  @media all and (max-width: 500px)
{
  .user-name {
    display: none;
  }
}
</style>
