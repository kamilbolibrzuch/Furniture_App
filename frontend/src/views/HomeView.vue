<template>
  <div>
   
    <!-- komponent nawigacji -->
    <div class="home ">
      <div class="text-center" id="background_" style="height: 10em">
        <h1 style=" color: rgba(235,0,105,255); padding-top: 25px; font-size: 55px; ">Strona Główna</h1>
      </div>

      <br />

      <!--Głowny layout-->
      <main class="my-5">
        <div class="container">
          <!--Ostatnio dodane Posty-->
          <section class="text-center">
            <h4 class="mb-5">
              <strong style="font-size: 30px; color: rgba(0,0,0);">Ostatnio dodane posty:</strong>
            </h4>

            <LatestPostsComponent></LatestPostsComponent>
          </section>


        </div>
      </main>
      <!--Main layout-->

      <!--Stopka-->
      <footer class="bg-light text-lg-start">
        <hr class="m-0" />


        <!-- Copyright -->
        <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
          © 2022 Copyright:
          <a class="text-dark">FurnitureApp.pl</a>
        </div>
        <!-- Copyright -->
      </footer>
      <!--Stopka-->
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/ui/Navbar.vue";
import LatestPostsComponent from "@/components/posts/LatestPostsComponent";
import { mdbRipple, MDBBtnGroup, MDBBtn } from "mdb-vue-ui-kit";
export default {
  name: "Home",
  data() {
    return {
    };
  },
  components: {
    Navbar,
    LatestPostsComponent,
    MDBBtnGroup,
    MDBBtn,
  },
  mounted(){
document.title = "Strona głowna";
  },

  directives: {
    mdbRipple,
  },
  methods: {

  },
};
</script>

<style>
#link {
  color: white;
  text-decoration: none;
}


#przycisk {
  transition: all 0.5s;
  cursor: pointer;
  font-size: 28px;
  font-family: "Molle", cursive;
}

#przycisk span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}

#przycisk span:after {
  content: "\00bb";
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}

#przycisk:hover span {
  padding-right: 25px;
}

#przycisk:hover span:after {
  opacity: 1;
  right: 0;
}
    
#background_ {
  background-color: rgb(255, 255, 255);
  background-size: cover;
}

@media screen and (max-width: 500px) {
  #background_ {

    background-size: cover;
  }
}
</style>
