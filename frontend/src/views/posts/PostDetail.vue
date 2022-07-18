<template>
  <div>
  
    <!-- komponent nawigacji -->
    <body>
      <div class="main-content" id="background">
        <!-- Header -->
        <div class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center" style=" height: 200px; background-color: rgba(235,0,105,255); background-size: cover; background-position: center top; ">
          <!-- Mask -->
          <div class="container-fluid d-flex align-items-center">
            <div class="row">
              <div class="col-lg-7 col-md-10">
                <h1 class="display-2 text-white" style="padding-left: 50px">
                  {{ post.name }}
                </h1>
                <br />
                <p></p>
              </div>
            </div>
          </div>
        </div>
        <div class="container p-0 mt--7">
          <div class="row">
            <div class="col-md-5 col-lg-7">
              <div class="card mb-3">
                <div class="card-body">
                  <div class="row">
                    <div class="col-lg-12 align-items-center">
                      <!-- -->
                      <div id="carouselExampleIndicators" class="carousel slide" data-mdb-ride="carousel">
                        <div class="carousel-indicators">
                          <button type="button" data-mdb-target="#carouselExampleIndicators" data-mdb-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>

                          <button type="button" data-mdb-target="#carouselExampleIndicators" v-for="i in rest_images_length" :data-mdb-slide-to="i" :aria-label="i"></button>
                        </div>
                        <div class="carousel-inner">
                          <div class="carousel-item active">
                            <img v-bind:src="first_image.get_image"  class="d-block w-100" :alt="first_image.name"/>
                          </div>
                          <div class="carousel-item" v-for="image in rest_images">
                            <img v-bind:src="image.get_image" class="d-block w-100"  :alt="image.name" />
                          </div>
                        </div>
                        <button class="carousel-control-prev" type="button" data-mdb-target="#carouselExampleIndicators" data-mdb-slide="prev">
                          <span class="carousel-control-prev-icon"  v-if="rest_images_length>0" aria-hidden="true"></span>
                          <span class="visually-hidden" v-if="rest_images_length>0">Previous</span>
                        </button>
                        <button
                          class="carousel-control-next"
                          type="button"
                          data-mdb-target="#carouselExampleIndicators" data-mdb-slide="next">
                          <span class="carousel-control-next-icon" v-if="rest_images_length>0" aria-hidden="true"></span>
                          <span class="visually-hidden" v-if="rest_images_length>0">Next</span>
                        </button>
                      </div>
                      <!-- -->
                    </div>
                  </div>
                  <hr />
                  <div class="row">
                    <div class="col-sm-3">
                      <h6 class="mb-0">opis</h6>
                    </div>
                    <div class="col-sm-9 text-secondary">
                      <p>{{ post.description }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-5 col-md-6 mb-6">
              <div class="card">
                <div class="card-body">
                  <div class="align-items-center text-center">
                    <p class="font-weight-bold text-dark">
                      Przykładowy napis
                    </p>

                    <div class="mt-3"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </body>
  </div>
</template>
<script>
import axios from "axios";
import Navbar from "@/components/ui/Navbar.vue";
export default {
  name: "PostDetail",
  data() {
    return {
      post: {},
      post_slug: "",
      first_image: "", //pierwsze zdjęcie w karuzeli ma ustawiony atrrybut active
      rest_images: [], //reszta zdjęć jest na pozostałych pozycjach
      rest_images_length: "",
    };
  },
  components: {
    Navbar,
  },
  beforeMount() {},
  mounted() {
    document.title = "Szczegóły Posta";
    this.getPost();
  },
  methods: {
    async getPost() {
      const post_slug = this.$route.params.post_slug;
      this.post_slug = post_slug;

      axios
        .get(`/api/furniture_app/post/${post_slug}/`)
        .then((response) => {
          this.post = response.data;

          this.first_image = this.post.image[0]; //1 zdjęcie do karuzeli
          for (
            let i = 1;
            i < this.post.image.length;
            i++ //pozostałe
          ) {
            this.rest_images.push(this.post.image[i]);
          } //zdjęcia
          this.rest_images_length = this.rest_images.length;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
