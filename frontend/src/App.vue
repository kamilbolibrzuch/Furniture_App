<template>
  <router-view/>
</template>
<script>
import axios from 'axios'
export default{
  data() {
    return{
      authenticated: false
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore') //commit uruchamia mutations z vuex o nazwie initializeStore
    const token = this.$store.state.token
    
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
