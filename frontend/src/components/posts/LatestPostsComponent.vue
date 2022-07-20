<template>
    <!--Posty-->
    <div class="row" >
        <div class="col-lg-3 col-md-6 mb-4 card-box" v-for="post in latestPosts" v-bind:key="post.id">
          <router-link v-bind:to="post.get_absolute_url">
            <MDBCard class="shadow-custom " style="border-radius: 10px;" >
              <div class="bg-image" >
              
                <MDBCardImg id="zdjecie" class="img-fluid" v-bind:src="post.image.at(-1).get_thumbnail"/>
              </div>
              <MDBCardBody class="card-body">
                <MDBCardTitle class="card-title" style="text-decoration: none; color:black;" >{{ post.name }}</MDBCardTitle>
                <MDBCardTitle class="card-title zdjecie-text1_post" >{{ post.name }}</MDBCardTitle><br>
                
                <span style="color: white"><router-link v-bind:to="post.get_absolute_url" class="btn" id="btn_post">szczegóły</router-link></span>
              </MDBCardBody>
            </MDBCard>
          </router-link>
        </div>
     <!--Psy-->

     <!-- Zobacz więcej postów -->
        <div class="col-lg-3 col-md-6 mb-4 card-box" >
          <MDBCard class="shadow-custom" style="border-radius: 10px;" id="background_post">
            <router-link to="/posts/1/order_by=from-newest" >
              <div class="bg-image">
                <div  id="zdj_wiecej" class="img-fluid">
                  <div id="wiecej_postow"><b><br>Zobacz więcej<br>raportów</b></div>
                </div>
              </div>
              <MDBCardBody class="card-body">
              </MDBCardBody>
            </router-link>
          </MDBCard>
        </div>
     <!-- ------------------- -->  
    </div>
</template>


<script>
import axios from 'axios'

import { MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg, MDBBtn, mdbRipple } from "mdb-vue-ui-kit";


export default {
    name: 'LatestPostsComponent',
    data(){
    return{
      latestPosts: [],
    }
  },
  components: {
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
    MDBCardText,
    MDBCardImg,
    MDBBtn
    
  },
  mounted() {
    this.getLatestPosts(),
    document.title = 'Zaadoptuj-zwierzaka'
  },
   methods: {
 
  
   async getLatestPosts() {
    
      await axios
        .get('api/furniture_app/latest-posts/')
        .then(response => {
          this.latestPosts = response.data          
        })
        .catch(error => {
          console.log(error)
        })
    }
}
}
</script>

<style>
.card-box {
  position: relative;
  display: flex;
	justify-content: space-around;
  align-items: flex-end;
	transition: 0.4s ease-out;
	box-shadow: 0px 7px 10px rgba(black, 0.5);
}
.card-box span {
  display: none;
  position: absolute;
  top: 45%;
  transform: translateY(-50%);
  left: 50%;
  transform: translateX(-50%);
}
.card-box:hover span{
  display: table-cell;  
}

.card-box:hover #zdjecie{
  -webkit-filter: blur(5px); 
}
.card-box:hover {
  transform: translateY(5px);
}

.bg-image{
  object-fit: cover;
}

.shadow-custom{
     box-shadow: 0 2px 20px 0 rgba(0, 0, 0, .25), 0 3px 8px 0px rgba(0, 0, 0, 0.13) !important;
}
.card-box:hover .zdjecie-text1_post,.card-box:hover .zdjecie-text2 {
  visibility: visible;
  opacity: 1;
}
.zdjecie-text1_post {
  font-size: 40px;
  position: absolute;
  top: 10%;
	left: 0;
	display: block;
	width: 100%;
	height: 100%;
	opacity: 0;
  visibility: hidden;
 
  text-shadow: white 0.1em 0.1em 0.2em;
   -webkit-text-fill-color: rgb(0,0,0);
  -webkit-text-stroke-color: rgb(255, 255, 255);
  -webkit-text-stroke-width: 0.50px; 
}

.zdjecie-text2 {
  font-size: 25px;
  position: absolute;
  top: 20%;
	left: 0;
	display: block;
	width: 100%;
	height: 100%;
	opacity: 0;
  visibility: hidden;
  color: black;
  text-shadow: white 0.1em 0.1em 0.2em
}

#btn_post {
  color: #ffff;
  text-decoration: none;
  background: rgba(190,190,190,255);
  padding: 30px;
  border-radius: 5px;
  display: inline-block;
  border: none;
  transition: all 0.4s ease 0s;
}
#btn_post:hover {
  background: rgba(235,0,105,255);
  
  color: aliceblue;
  -webkit-box-shadow: 0 5px 40px -10px rgba(0, 0, 0, 0.57);
  -moz-box-shadow: 0 5px 40px -10px rgba(0, 0, 0, 0.57);
  box-shadow: 5px 40px -10px rgba(0, 0, 0, 0.57);
  transition: all 0.4s ease 0s;
}

#wiecej_postow {

  font-size: 50px;
  color:rgba(235,0,105,255);
  padding: 20px 0;
  text-align: center;
  font-family: Roboto, Helvetica, Arial, sans-serif;
}

#zdj_wiecej {
border-radius: 10px;
  width: 350px;
  height: 356px;
}

#zdjecie {
          width: 350px;
          height: 300px;
}

</style>