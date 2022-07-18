<template>
<navbar v-if="$store.state.user.isAuthenticated"></navbar>
  <router-view/>
</template>
<script>
import Navbar from "@/components/ui/Navbar.vue";
import axios from 'axios'

export default{
  data() {
    return{
      authenticated: false
    }
  },
  components: {
    Navbar,},
  beforeCreate() {
    this.$store.commit('initializeStore') //commit uruchamia mutations z vuex o nazwie initializeStore
    const token = this.$store.state.user.token
    
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token" + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""   //resetowanie tokenu 
    }
  },

}
</script>
<style lang="scss">
@import '~@/../mdb/scss/index.free.scss';


</style>
