<template>
  <div>
    <div class="container-fluid ps-md-0">
      <div class="row g-0">
        <div class="d-none d-md-flex col-md-5 col-lg-6 mx-auto"></div>
        <div class="col-md-7 col-lg-6">
          <div class="login d-flex align-items-center py-5">
            <div class="container">
              <div class="row">
                <div class="col-md-9 col-lg-8 mx-auto">
                  <h3 v-if="!alert" class="login-heading mb-4" style=" font-family: 'Libre Baskerville', serif; font-size: 250%;">Dodaj Raport</h3>
<!-- Alert informujacy o dodaniu raportu-->
                  <div class="alert alert-info" v-if="alert">
                    <p>
                      <br />
                      Raport został utworzony!<br />
                      Przejdź na stronę
                      <b><router-link to="/">główną.</router-link></b>
                      <br />
                      Twój post pojawi się w sekcji ostatnio dodane rapoty.
                    </p>
                  </div>
<!-- Alert -->
<!-- Formularz -->
                  <form @submit.prevent="submitForm" enctype="multipart/form-data" v-if="!alert">
                    <div class="form-floating mb-3">
                      <div class="form__group">
                        <input type="text" id="postname" class="form__field" placeholder="Nazwa postu" v-model="name" required />
                        <label for="postname" class="form__label">* Nazwa postu</label>
                      </div>
                    </div>

                    <div class="form-floating mb-3">
                      <div class="form__group">
                        <textarea id="description" class="form-control" rows="5" placeholder="* Opis: " v-model="description" required>
                        </textarea>
                      </div>
                    </div>

                    <br /><br />

                    <input id="file-upload" type="file" class="form-control" accept=".jpg,.jpeg,.png" multiple @change="uploadImage" required/>
                    <div v-for="(image, key) in images" :key="key" class="wrapper-thumb" >
                      <div id="img-preview">
                        <img :src="'image'" ref="image" class="img-preview-thumb" alt="zdj"  v-on:click=" (e) => e.target.classList.toggle('Imgpreview-zoom')"/>
                        <div  @click="removeImage(image, key)"><i class="fas fa-times-circle fa-xl remove-btn"></i></div>
                      </div>
                    </div>
                <br />
<!-- Alert jeśli usuneliśmy wszystkie zdjęcia (ww podglądzie)-->
                <div class="alert alert-danger" v-if="noImagesAlert">
                    <p>
                      <br />
                      Usunięto wszystkie zdjęcia!<br />
                      Musisz dodać zdjęcie aby utworzyć raport.
                      <br />
                    </p>
                  </div>
<!-- Alert -->
                    <br />
                    <p style="color: #9b9b9b">
                      * Pola oznaczone gwiazdką są obowiązkowe do poprawnego
                      wypełnienia formularza, jeśli pole nie jest obowiązkowe
                      możesz pozostawić je puste.
                    </p>
                    <br />
                    <div class="d-grid">
                      <MDBBtn class="btn btn-lg" rounded type="submit" style="background-color: #4be1e1; color: white">Dodaj raport</MDBBtn>
                    </div>
                  </form>
                  <!-- Formularz -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FormData from "form-data";
import axios from "axios";
import { MDBBtn} from "mdb-vue-ui-kit";
import Navbar from "@/components/ui/Navbar.vue";
import $ from "jquery";
export default {
  name: "AddPost",
  components: {
    MDBBtn,
    Navbar,
  },
  data() {
    return {
      name: "",
      description: "",
      images: [],
      token: "",
      imagePreview: "",
      alert: false,
      noImagesAlert: false,
      used_input: 0
    };
  },
  mounted() {
    document.title = "Dodaj Raport";
  },
  computed: {
    getToken() {
      return this.$store.state.user.token;
    },
  },
  methods: {
    submitForm() {
      if(this.images.length==0){this.noImagesAlert = true;}
      else{this.noImagesAlert=false;
      //!!!!!!NAJPIERW DODANIE DO POSTA/////////////////////////////
      let formData = new FormData();
      formData.append("name", this.name);
      formData.append("description", this.description);

      axios
        .post(`/api/furniture_app/add-post/`, formData, {
          headers: {
            Authorization: `Token ${this.$store.state.user.token}`,
          },
        })
        //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/
        .then((res) => {
          console.log(res);
          //~~~~~~~~~~~NASTEPNIE DODANIE ZDJEĆ/////////////////////////////////
          let imageformData = new FormData();
          for (const i of Object.keys(this.images)) {
            //imageformData.append("image", this.image[i]);
            imageformData.append("image", this.images[i]);
            imageformData.append("name", this.images[i].name);
          }
          axios
            .post(`/api/furniture_app/add-post/image/`, imageformData, {
              headers: {
                Authorization: `Token ${this.$store.state.user.token}`,
              },
            })
            //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
            .then((res) => {
              console.log(res);
              this.alert = true;
            })
            .catch((error) => {
              console.log(error);
            });
        })
        .catch((error) => { console.log(error); });
      }
    },
    uploadImage(e) {
      this.noImagesAlert=false;
      this.images.length=0;
      this.refreshImg();
      let selectedFiles = e.target.files;
      for (let i = 0; i < selectedFiles.length; i++) {
        this.images.push(selectedFiles[i]);
      }
      this.refreshImg();
      
    },
    refreshImg() {
      if(this.images.length!=0){
      for (let i = 0; i < this.images.length; i++) {
        let reader = new FileReader();
        reader.onload = (e) => {
          this.$refs.image[i].src = reader.result;
        };
        reader.readAsDataURL(this.images[i]);
      }
      }
    },
    removeImage(image, index) {
      if(this.images.length!=0){
      this.images.splice(index, 1);
      this.refreshImg();
      }
    },
  },
};
</script>

<style>
.uploading-image {
  display: flex;
}

.input-file {
  opacity: 0;
  width: 100%;
  height: 200px;
  position: absolute;
  cursor: pointer;
}

.my-select {
  background-color: white;
  color: #009788;
  border-color: #009788;
  border-radius: 20px;
  padding: 6px 20px;
}

/* css do wyglądu inputów*/
.form__group {
  position: relative;
  padding: 15px 0 0;
  margin-top: 10px;
}

.form__field {
  font-family: inherit;
  width: 100%;
  border: 0;
  border-bottom: 1px solid #d2d2d2;
  outline: 0;
  font-size: 16px;
  color: #212121;
  padding: 7px 0;
  background: transparent;
  transition: border-color 0.2s;
}

.form__field::placeholder {
  color: transparent;
}

.form__field:placeholder-shown ~ .form__label {
  font-size: 16px;
  cursor: text;
  top: 20px;
}

label,
.form__field:focus ~ .form__label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 12px;
  color: #9b9b9b;
}

.form__field:focus ~ .form__label {
  color: #009788;
}

.form__field:focus {
  padding-bottom: 6px;
  border-bottom: 2px solid #009788;
}

/*img-podgląd*/

.img-thumbs {
  border: 1px solid #ccc;
  border-radius: 0.25rem;
  margin: 2.5rem 0;
  padding: 1.75rem;

  border-radius: 10px;
  cursor: zoom-in;
}
.img-thumbs-hidden {
  display: none;
}

.wrapper-thumb {
  position: relative;
  display: inline-block;
  margin-left: 3rem;
  margin-top: 1rem;

  justify-content: space-around;
}
/**/

img.Imgpreview-zoom {
  -ms-transform: scale(1.9);
  -webkit-transform: scale(1.9);
  transform: scale(1.9);
  z-index: 1090 !important;
  cursor: zoom-out !important;
  position: relative;
}

.img-preview-thumb {
  background: #fff;
  border: 1px solid none;
  border-radius: 0.25rem;
  box-shadow: 0.125rem 0.125rem 0.0625rem rgba(0, 0, 0, 0.12);
  margin-right: 1rem;
  margin-left: 15%;
  margin-top: 1rem;
  max-width: 200px;
  padding: 0.25rem;
  cursor: zoom-in;

}

.remove-btn {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  
  top: 15px;
  right: -18px;

  cursor: pointer;
  color: red;
}

.remove-btn:hover {
  box-shadow: 0px 0px 3px grey;
  transition: all 0.3s ease-in-out;
}
</style>
