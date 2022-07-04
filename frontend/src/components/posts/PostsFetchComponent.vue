<template>
<div>postfetch..</div>
</template>

<script>
import axios from "axios";

import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBCardText,
  MDBCardImg,
  MDBBtn,
} from "mdb-vue-ui-kit";
export default {
    name: "PostsFetchComponent",
    data () {
        return {
            data: [],
            order_by: this.$route.params.order_by,
            pagesize: 4,
        }
    },
    components: {   
        MDBCard,MDBCardBody,MDBCardTitle,MDBCardText,MDBCardImg,MDBBtn,    
    },
    beforeMount() {
        this.order_by = this.$route.params.order_by;
    }
}



</script>