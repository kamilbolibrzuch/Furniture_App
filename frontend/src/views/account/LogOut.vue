<template>
</template>
<script>

export default {
    name: "LogOut",
    data(){
        return{

        }
    },
    mounted(){
        this.LogOut();
    },
    methods: {
        async LogOut(){
            this.$store.commit({type:'LogOutUser'}) //metoda w storze odpowiedzialna za wylogowanie
                           window.location.href = "/" // po wylogowaniu jeśli wszystko się udało przenosimy na strone dashboard
        }
    }
}



</script>