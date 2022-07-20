<template>
  <div class="container-fluid ps-md-0">
    <div class="row g-0">
      <div class="d-none d-md-flex col-md-6 col-lg-6 mx-auto" ><img src="../../assets/forgot.jpg" class="img-fluid"></div>
      <div class="col-md-6 col-lg-6">
        <div class="login d-flex align-items-center py-5">
          <div class="container-fluid">
            <div class="row">
              <div class="col-md-6 col-lg-8 mx-auto">
                <!-- Alert -->
                <div class="alert alert-info" v-if="alert">
                  <p>Wiadomość wysłano na Twój adres e-mail.</p>
                </div>
                <!-- -->
                  <!-- Errory -->
                  <div class="alert alert-danger" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">
                      {{ error }}
                    </p>
                  </div>
                <h3 class="login-heading mb-4" style=" font-family: 'Libre Baskerville', serif; font-size: 250%;">
                  Nie pamiętasz hasła?
                </h3>

                <div>
                  Wystarczy, że podasz swój e-mail, a my pomożemy Ci ustawić
                  nowe hasło.
                </div>
                <form @submit.prevent="submitForm">
                  <div class="form-floating mb-3">
                    <div class="form__group_blue">
                      <input type="email" id="email" class="form__field_blue" placeholder="adres e-mail" v-model="email" required />
                      <label for="email" class="form__label_blue">adres e-mail</label >
                    </div>
                  </div>
                  <br />
                  <div class="d-grid">
                    <MDBBtn class="btn btn-lg" rounded type="submit" style="background-color: #b1e7e9; color: black"><b>Wyślij link na adres e-mail</b></MDBBtn>
                    <div class="text-center">
                      <br />
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from "axios";

import { MDBBtn } from "mdb-vue-ui-kit";

export default {
  name: "LogIn",
  components: {
    MDBBtn,
  },
  data() {
    return {
      email: "",
      alert: false,
      errors: []
    };
  },

  mounted() {
    document.title = "Nie pamiętasz hasła";
    window.scrollTo(0,document.body.scrollHeight);
  },
  methods: {
    async submitForm() {
      const formData = {
        email: this.email,
      };
      await axios
        .post("api/furniture_app/users/reset_password/", formData)
        .then((response) => {
          console.log(response);
          this.alert = true;
        })
        .catch((error) => {
          this.errors.push(error.response.data[0]);
        });
    },
  },
};
</script>

<style>
.login {
  min-height: 100vh;
}

#bg-image {
  background-size: cover;
  background-position: center;
  background-color: #009788;
}

.login-heading {
  font-weight: 300;
}

.btn-login {
  font-size: 0.9rem;
  letter-spacing: 0.05rem;
  padding: 0.75rem 1rem;
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
