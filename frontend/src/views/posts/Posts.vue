<template>
  <div>
    <navbar></navbar>
    <!-- komponent nawigacji -->
    <div class="home">
      <div  class=" text-center bg-light" style="height: 13em">
        <h1 style="color:black; font-size: 50px;">Posty</h1>
      </div>

      <main class="my-5">
        <div class="text-center"></div>
        <section class="text-center">
          <div class="container-fluid">
            <div class="row">
              <div><PostsFetchComponentVue></PostsFetchComponentVue></div>
            </div>
          </div>
        </section>
      </main>

      <!--Footer-->
      <footer class="bg-light text-lg-start">
        <hr class="m-0" />

        <!-- Copyright -->
        <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
          © 2022 Copyright:
          <a class="text-dark">FurnitureApp.pl</a>
        </div>
        <!-- Copyright -->
      </footer>
      <!--Footer-->
    </div>
  </div>
</template>

<script>

import Navbar from "@/components/ui/Navbar.vue";
import PostsFetchComponentVue from "@/components/posts/PostsFetchComponent.vue";
import { mdbRipple, MDBBtn } from "mdb-vue-ui-kit";

export default {
  name: "Posts",
  data() {
    return {};
  },
  components: {
    Navbar,
    PostsFetchComponentVue,
    MDBBtn,
  },
  mounted() {
    document.title = "Posty";
  },
  methods: {},
  directives: {
    mdbRipple,
  },
};
</script>

<style>
</style>
