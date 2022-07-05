<template>
  <div class="row">
    <!--~~~~~~~~~~SORTOWANIE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
    <div class="col-lg-10 col-md-7 mb-4 mx-auto">
      Sortuj:
      <div class="col-lg-3 col-md-7 mb-3" style="display: inline-block">
        <select class="form-control" id="sortowanie" name="sortowanie" @change="sortowanie($event)">
          <option>Data: od najnowszych</option>
          <option>Data: od najstarszych</option>
          <option>Alfabetycznie: A-Z</option>
          <option>Alfabetycznie: Z-A</option>
        </select>
      </div>
      <!--~~~~~~~~~~SORTOWANIE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
      <!--~~~~~~~~~~POSTY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
      <br />
      <br />
      <h2 v-if="data.results == ''" style="color: red">
        Niestety nie znaleziono żadnych wyników, dla zastosowanych filtrów.
      </h2>
      <br />
      <div class="row">
        <div class="col-lg-3 col-md-6 mb-4 card-box" v-for="post in data.results" v-bind:key="post.id">
          <router-link v-bind:to="post.get_absolute_url">
            <MDBCard class="shadow-custom" style="border-radius: 10px">
              <div class="bg-image">
                <MDBCardImg id="zdjecie" class="img-fluid" v-bind:src="post.image.at(-1).get_thumbnail"/>
              </div>
              <MDBCardBody class="card-body">
                <MDBCardTitle class="card-title" style="text-decoration: none; color: black">{{ post.name }}</MDBCardTitle>
                <MDBCardTitle class="card-title zdjecie-text1_post">{{post.name}}</MDBCardTitle>
                <br />
                <span style="color: white">
                  <router-link v-bind:to="post.get_absolute_url" class="btn" id="btn_post">szczegóły</router-link>
                  </span>
              </MDBCardBody>
            </MDBCard>
          </router-link>
        </div>
        <!--~~~~~~~~~~POSTY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
        <!--~~~~~~~~~~PAGINACJA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
        <nav v-if="data.results != ''" aria-label="pagination" class="pagination justify-content-center" style="margin: 20px 0">
          <ul class="pagination">
            <li class="page-item" v-if="parseInt(this.$route.params.pagenumber) > 1">
              <a class="page-link" :href="'/posts/' +(parseInt(this.$route.params.pagenumber) - 1) +'/' +order_by">Poprzednia</a>
            </li>
            <li v-for="page in data.page_numbers" v-bind:class="[ pageItemClass, page === parseInt(this.$route.params.pagenumber) ? activeClass : '',]">
              <a class="page-link" :href="'/posts/' + page + '/' + order_by">{{ page}}</a>
            </li>
            <li class="page-item" v-if="data.next_page">
              <a class="page-link" :href=" '/posts/' + (parseInt(this.$route.params.pagenumber) + 1) + '/' + order_by" >Następna</a>
            </li>
          </ul>
        </nav>
        <!--~~~~~~~~~~PAGINACJA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg, MDBBtn,} from "mdb-vue-ui-kit";
export default {
  name: "PostsFetchComponent",
  data() {
    return {
      data: [],
      order_by: this.$route.params.order_by,
      pagesize: 4,
      pageItemClass: "page-item",
      activeClass: "active",
      selected_sort: "",
    };
  },
  components: {
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
    MDBCardText,
    MDBCardImg,
    MDBBtn,
  },
  mounted() {
    this.order_by = this.$route.params.order_by;
    if (this.order_by === "order_by=from-newest" || this.order_by ==="from-newest") { document.getElementById("sortowanie").options[0].setAttribute("selected", true); this.order_by="from-newest";}     //ustawienie na selectcie wybranej opcji zgodnie z parametrem  oraz ustawienie
    if (this.order_by === "order_by=from-oldest" || this.order_by ==="from-oldest") { document.getElementById("sortowanie").options[1].setAttribute("selected", true); this.order_by="from-oldest";}     // order by aby nie występowało podójnie tj. order_by=from-newest&order_by=from-newest
    if (this.order_by === "order_by=alphabetical" || this.order_by ==="alphabetical") { document.getElementById("sortowanie").options[2].setAttribute("selected", true); this.order_by="alphabetical";}     
    if (this.order_by === "order_by=alphabetical-reverse" || this.order_by ==="alphabetical-reverse") { document.getElementById("sortowanie").options[3].setAttribute("selected", true); this.order_by="alphabetical-reverse";} 
    this.getPosts();
  },
  methods: {
    async getPosts() {

      await axios
        .post(
          `api/furniture_app/posts/?page_number=${this.$route.params.pagenumber}&page_size=${this.pagesize}&order_by=${this.order_by}`
        )
        .then((response) => {
          this.data = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    sortowanie(event) {
        this.selected_sort = event.target.value;
        if(this.selected_sort === "Data: od najnowszych"){this.order_by = "from-newest"}
        if(this.selected_sort === "Data: od najstarszych"){this.order_by = "from-oldest"}
        if(this.selected_sort === "Alfabetycznie: A-Z"){this.order_by = "alphabetical"}
        if(this.selected_sort === "Alfabetycznie: Z-A"){this.order_by = "alphabetical-reverse"}
        this.getPosts();
    }
  },
};
</script>
