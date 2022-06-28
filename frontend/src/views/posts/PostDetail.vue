<template>
<div>
    <navbar></navbar>
    <!-- komponent nawigacji -->
    <div>{{this.$route.params.post_slug}}</div>
</div>
</template>
<script>
import axios from "axios";
import Navbar from "@/components/ui/Navbar.vue";
export default {
    name: "PostDetail",
    data(){
        return {
            post: {},
            post_slug: "",
            
        };
    },
    components: {
    Navbar,
    },
      beforeMount() {
  
  },
    mounted(){
    document.title = "Szczegóły Posta";
    this.getPost();
    },
    methods: {
        async getPost(){
            const post_slug = this.$route.params.post_slug;
            this.post_slug=post_slug
            
            axios
                .get(`/api/furniture_app/post/${post_slug}/`)
                .then((response) =>{
                    
                    this.post = response.data;
                    console.log(this.post);
                })
                .catch((error) => {
                    console.log(error);
                })
        }
    }

}

</script>