<template>
  <div>
    <navbar></navbar>
    <!-- komponent nawigacji -->
    <div class="container-fluid ps-md-0">
      <div class="row g-0">
        <div class="d-none d-md-flex col-md-5 col-lg-6 mx-auto"></div>
        <div class="col-md-7 col-lg-6">
          <div class="login d-flex align-items-center py-5">
            <div class="container">
              <div class="row">
                <div class="col-md-9 col-lg-8 mx-auto">
                  <h3 v-if="!alert" class="login-heading mb-4" style=" font-family: 'Libre Baskerville', serif; font-size: 250%;"> Dodaj Post </h3>
                  <!-- Alert -->
                  <div class="alert alert-info" v-if="alert">
                    <p>
                      <br /> Post został utworzony!<br /> Przejdź na stronę
                      <b><router-link to="/">główną.</router-link></b>
                      <br />
                      Twój post pojawi się w sekcji ostatnio dodane posty.
                    </p>
                  </div>
                  <!-- Alert -->
                  <!-- Formularz -->
                  <form @submit.prevent="submitForm" v-if="!alert">
                    <div class="form-floating mb-3">
                      <div class="form__group">
                        <input type="text" id="postname" class="form__field" placeholder="Nazwa postu" v-model="name" required />
                        <label for="catname" class="form__label">* Nazwa postu</label>
                      </div>
                    </div>

                    <div class="form-floating mb-3">
                      <div class="form__group">
                        <textarea id="description" class="form-control" rows="5"
                          placeholder="* Opis: " v-model="description" required>
                        </textarea>
                      </div>
                    </div>

                    <br /><br />
                    <div class="container">
                      <div class="form-group">
                        <div class="input-group mb-3">
                          <input type="file" class="form-control" accept=".jpg,.jpeg,.png" @change="handleFileUpload($event)"/>
                        </div>
                        <div class="image-preview" v-if="imagePreview.length > 0">
                          <img class="preview" :src="imagePreview" />
                        </div>
                      </div>
                    </div>

                    <p style="color: #9b9b9b">
                      * Pola oznaczone gwiazdką są obowiązkowe do poprawnego
                      wypełnienia formularza, jeśli pole nie jest obowiązkowe
                      możesz pozostawić je puste.
                    </p>
                    <br />
                    <div class="d-grid">
                      <MDBBtn class="btn btn-lg" rounded type="submit" style="background-color: #4be1e1; color: white">Dodaj post</MDBBtn>
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
import { MDBBtn, MDBInput } from "mdb-vue-ui-kit";
import Navbar from "@/components/ui/Navbar.vue";
export default {
  name: "AddPost",
  components: {
    MDBBtn,
    MDBInput,
    Navbar,
  },
  data() {
    return {
      name: "",
      description: "",
      image: "",
      token: "",
      imagePreview: "",
      alert: false,
    };
  },
  mounted() {
    document.title = "Dodaj Post";
  },
  computed: {
    getToken() {
      return this.$store.state.token;
    },
  },
  methods: {
    submitForm() {
      let formData = new FormData();
      formData.append("name", this.name);
      formData.append("image", this.image);
      formData.append("description", this.description);

      axios
        .post(`/api/furniture_app/add-post/`, formData, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
        .then((res) => {
          console.log(res);
          this.alert = true;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    handleFileUpload(event) {
      var input = event.target; //jeśli mamy plik

      if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = (e) => {
          this.imagePreview = e.target.result;
        };

        reader.readAsDataURL(input.files[0]); //base64
      }
      this.image = event.target.files[0];
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

img.preview {
  width: 300px;
  background-color: white;
  border: 1px solid black;
  padding: 5px;
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
</style>
