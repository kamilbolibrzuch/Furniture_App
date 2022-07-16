<template>

    <MDBNavbar expand="lg" dark container style="background-color: rgba(190,190,190,255);">
    <MDBNavbarBrand href="/" id="Logo"><img src="/static/logo.png" style="height: 40px;" alt="logo" ></MDBNavbarBrand>
    
    <MDBNavbarToggler @click="collapse1 = !collapse1" target="#navbarSupportedContent">
    </MDBNavbarToggler>
    <MDBCollapse v-model="collapse1" id="navbarSupportedContent">
      <MDBNavbarNav center class="mb-2 mb-lg-0">
        <MDBNavbarItem to="/add-post" >
          <router-link to="/add-post" style="color:white;">Dodaj post</router-link>
        </MDBNavbarItem>
        <MDBNavbarItem to="/posts/1/order_by=from-newest" >
          <router-link to="/posts/1/order_by=from-newest" style="color:white;">Przeglądaj posty</router-link>
        </MDBNavbarItem>
        <MDBNavbarNav>

        </MDBNavbarNav>
                <MDBNavbarItem to="/log-out" >
          <router-link to="/log-out" style="color:white;">Wyloguj</router-link>
        </MDBNavbarItem>

      </MDBNavbarNav>
      
    </MDBCollapse>
  </MDBNavbar>
</template>

<script>
import {
    MDBBtn,
    MDBIcon,
    MDBNavbar,
    MDBNavbarToggler,
    MDBNavbarBrand,
    MDBNavbarNav,
    MDBNavbarItem,
    MDBCollapse,
    MDBDropdown,
    MDBDropdownToggle,
    MDBDropdownMenu,
    MDBDropdownItem
  } from 'mdb-vue-ui-kit';
  import { ref } from 'vue';


export default {
  name: 'Navbar',
  components: {
    MDBBtn,
    MDBIcon,
    MDBNavbar,
    MDBNavbarToggler,
    MDBNavbarBrand,
    MDBNavbarNav,
    MDBNavbarItem,
    MDBCollapse,
    MDBDropdown,
    MDBDropdownToggle,
    MDBDropdownMenu,
    MDBDropdownItem,


  },    
    setup() {

      const collapse1 = ref(false);   //metody aby animacje działały (dropdown)
      const dropdown1 = ref(false);

      return {
        collapse1,
        dropdown1
      }
      
    },
    data () {
  return {
    publicPath: process.env.BASE_URL
  }
}
    



    
    
}

</script>

<style>

</style>

