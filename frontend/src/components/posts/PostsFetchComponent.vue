<template>
  <div class="row">
    <div class="container-fluid">
      <div v-if="searching">
        <div  class="p-5 text-center bg-light">
          <h1 class="mb-3 h2"> Wyszukiwana fraza: "<b>{{ query }}</b>"</h1>
            </div>
            <br />
          </div>
      <div class="d-flex justify-content-center">
                    
      <!--~~~~~~~~~~WYSZUKIWANIE  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
        <form class="d-flex input-group" @submit.prevent="Search" style="width: 320px;" >
          <input type="text" class="form-control" placeholder="Wyszukaj" aria-label="Wyszukaj" name="query" id="query" v-model="query" v-on:input="reset" />
          <button class="btn btn-dark" style="background-color: rgba(235,0,105,255);">szukaj</button>
        </form>
      <!--~~~~~~~~~~WYSZUKIWANIE  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
      </div>
    </div>
    <!--~~~~~~~~~~SORTOWANIE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
    
    <div  class="container">  
      <br/> 
      <p style="padding-right: 20%; color: black;">Sortuj:</p>
        <div class="row">
      <div class="col"  style="padding-left: 16%;">
      
        <select class="form-select-lg"  id="sortowanie" name="sortowanie" @change="sortowanie($event)">
          <option>Data: od najnowszych</option>
          <option>Data: od najstarszych</option>
          <option>Alfabetycznie: A-Z</option>
          <option>Alfabetycznie: Z-A</option>
        </select>
      </div>
    <!--~~~~~~~~~~WYBÓR WIDOKU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->  
    <div class="col bar" >
		<a class="list-icon" v-bind:class="{ 'active': layout == 'list'}" v-on:click="layout = 'list'" data-toggle="tooltip"  title="Widok listy"></a>
		<a class="grid-icon" v-bind:class="{ 'active': layout == 'grid'}" v-on:click="layout = 'grid'" data-toggle="tooltip"  title="Widok kafelkowy"></a>
	</div>
</div>
<br/>
    <!--~~~~~~~~~~WYBÓR WIDOKU~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ --> 
      <!--~~~~~~~~~~SORTOWANIE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->

    <!--~~~~~~~~~~POSTY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
      <!--~~~~~~~~~~WIDOK LISTY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ --> 
      <div class="row">
        <ul v-if="layout == 'list'" class="list">
            <li v-for="post in data.results" v-bind:key="post.id" >
            <router-link v-bind:to="post.get_absolute_url" >
                <img v-bind:src="post.image.at(-1).get_thumbnail" />
                <p style="text-decoration: none; color: black">{{post.name}}</p>
            </router-link>
            </li>
        </ul>
        <br />
        <br />
        <h2 v-if="data.results == ''" style="color: red">
            Niestety nie znaleziono żadnych wyników.
        </h2>
        <h2 v-if="data.results == ''&& searching" style="color: red">
            Upewnij się że wpisana fraza jest poprawna i spróbuj ponownie.
        </h2>
        <br />
      <!--~~~~~~~~~~WIDOK LISTY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
      <!--~~~~~~~~~~WIDOK KAFELKÓW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
        <div class="col-lg-3 col-md-6 mb-4 card-box" v-for="post in data.results" v-bind:key="post.id" >
          <router-link v-bind:to="post.get_absolute_url">
            <MDBCard class="shadow-custom" style="border-radius: 10px" v-if="layout =='grid'">
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
      <!--~~~~~~~~~~WIDOK KAFELKÓW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ -->
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
      layout: 'grid',
      query: '',
      searching: false
    };
  },
  components: { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg, MDBBtn, },
  mounted() {
    this.order_by = this.$route.params.order_by;
    if (this.order_by === "order_by=from-newest" || this.order_by ==="from-newest") { document.getElementById("sortowanie").options[0].setAttribute("selected", true); this.order_by="from-newest";}     //ustawienie na selectcie wybranej opcji zgodnie z parametrem  oraz ustawienie
    if (this.order_by === "order_by=from-oldest" || this.order_by ==="from-oldest") { document.getElementById("sortowanie").options[1].setAttribute("selected", true); this.order_by="from-oldest";}     // order by aby nie występowało podójnie tj. order_by=from-newest&order_by=from-newest
    if (this.order_by === "order_by=alphabetical" || this.order_by ==="alphabetical") { document.getElementById("sortowanie").options[2].setAttribute("selected", true); this.order_by="alphabetical";}     
    if (this.order_by === "order_by=alphabetical-reverse" || this.order_by ==="alphabetical-reverse") { document.getElementById("sortowanie").options[3].setAttribute("selected", true); this.order_by="alphabetical-reverse";} 
    
    this.query = this.$store.state.search.query;
    if(this.query!= ''){this.Search();}else{this.getPosts();}
    if(this.query== ''){this.$store.commit("removeQuery");}
  },
  methods: {
    async getPosts() {

      await axios
        .post(`api/furniture_app/posts/?page_number=${this.$route.params.pagenumber}&page_size=${this.pagesize}&order_by=${this.order_by}` )
        .then((response) => {
          this.data = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    
    async Search(){
      if(this.query==''){this.$store.commit("removeQuery"); this.getPosts();}else{
      await axios
        .post(`api/furniture_app/posts/search/?page_number=${this.$route.params.pagenumber}&page_size=${this.pagesize}&order_by=${this.order_by}`,
        { query: this.query }, )
        .then((response) => {
          this.data = response.data;
          this.searching = true;
          this.$store.commit("setQuery", this.query);
          console.log(this.data);
          
          
        })
        .catch((error) => {
          console.log(error);
        });
      }

    },
    reset(){this.searching=false;},
    sortowanie(event) {
        this.selected_sort = event.target.value;
        if(this.selected_sort === "Data: od najnowszych"){this.order_by = "from-newest"}
        if(this.selected_sort === "Data: od najstarszych"){this.order_by = "from-oldest"}
        if(this.selected_sort === "Alfabetycznie: A-Z"){this.order_by = "alphabetical"}
        if(this.selected_sort === "Alfabetycznie: Z-A"){this.order_by = "alphabetical-reverse"}
        if(this.query!= ''){this.Search();}else{this.getPosts();}
    }
  },
};
</script>



<style>
/*-------------------------
	Wybo widoku (kafelki/lista)
--------------------------*/
.bar a{
	background:#bebebe center center no-repeat;
	width:35px;
	height:35px;
	display:inline-block;
	
	margin-right:5px;
	
	cursor:pointer;
}

.bar a.active{
	background-color:rgba(235,0,105,255);
}

.bar a.list-icon{
	background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkYzNkFCQ0ZBMTBCRTExRTM5NDk4RDFEM0E5RkQ1NEZCIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkYzNkFCQ0ZCMTBCRTExRTM5NDk4RDFEM0E5RkQ1NEZCIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6RjM2QUJDRjgxMEJFMTFFMzk0OThEMUQzQTlGRDU0RkIiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6RjM2QUJDRjkxMEJFMTFFMzk0OThEMUQzQTlGRDU0RkIiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz7h1bLqAAAAWUlEQVR42mL8////BwYGBn4GCACxBRlIAIxAA/4jaXoPEkMyjJ+A/g9MDJQBRhYg8RFqMwg8RJIUINYLFDmBUi+ADQAF1n8ofk9yIAy6WPg4GgtDMRYAAgwAdLYwLAoIwPgAAAAASUVORK5CYII=);
}

.bar a.grid-icon{
	background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjBEQkMyQzE0MTBCRjExRTNBMDlGRTYyOTlBNDdCN0I4IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjBEQkMyQzE1MTBCRjExRTNBMDlGRTYyOTlBNDdCN0I4Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MERCQzJDMTIxMEJGMTFFM0EwOUZFNjI5OUE0N0I3QjgiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MERCQzJDMTMxMEJGMTFFM0EwOUZFNjI5OUE0N0I3QjgiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4MjPshAAAAXklEQVR42mL4////h/8I8B6IGaCYKHFGEMnAwCDIAAHvgZgRyiZKnImBQsACxB+hNoDAQyQ5osQZIT4gH1DsBZABH6AB8x/JaQzEig++WPiII7Rxio/GwmCIBYAAAwAwVIzMp1R0aQAAAABJRU5ErkJggg==);
}

/*-------------------------
	Widok listy
--------------------------*/

ul.list{
	list-style: none;
	width: 100%;
	margin: 0 auto;
	text-align: right;
}

ul.list li{
	border-bottom: 1px solid #ddd;
	padding: 10px;
	overflow: hidden;
}

ul.list li img{
	width:200px;
	height:200px;
	float:left;
	border:none;
}

ul.list li p{
	margin-left: 60%;
	font-weight: bold;
	
}
/*---------------------
  Paginacja
------------------------*/
.pagination > .active > a
{
    color: white;
    background-color: rgba(235,0,105,255) !Important;
    border: solid 1px rgba(235,0,105,255) !Important;
}

.pagination > .active > a:hover
{
    background-color: rgba(235,0,105,255) !Important;
    border: solid 1px rgba(235,0,105,255);
}


</style>
