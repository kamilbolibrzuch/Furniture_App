<template>
  <div class="container-fluid ps-md-0">
    <div class="row g-0">
      <div class="d-none d-md-flex col-md-6 col-lg-6 mx-auto" id="bg-image"></div>
      <div class="col-md-6 col-lg-6">
        <div class="login d-flex align-items-center py-5">
          <div class="container">
            <div class="row">
              <div class="col-md-9 col-lg-8 mx-auto">
                <!-- Alert -->
                <div class="alert alert-info" v-if="alert">
                  <p>
                    Twoje hasło zostało zmienione.<br />
                    Przejdź na stronę

                    <b><router-link to="/log-in">logowania</router-link></b> aby się
                    zalogować.
                  </p>
                </div>
                                     <!-- Alerty -->     
                        <div class="alert alert-info" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                <!-- -->
                <h3 class="login-heading mb-4" style=" font-family: 'Libre Baskerville', serif; font-size: 250%;">
                  Zmiana hasła
                </h3>

                <div>
                  Wypełnij poniższy formularz, aby zmienić Twoje hasło.
                </div>

                <form @submit.prevent="submitForm">
                  <div class="form__group_blue">
                    <div class="form__group_blue">
                      <input type="password" id="new_password" class="form__field_blue" placeholder="Nowe hasło" v-model="new_password" required/>
                      <label for="new_password" class="form__label_blue">Nowe hasło</label>
                    </div>
                  </div>

                  <div class="form-floating mb-3">
                    <div class="form__group_blue">
                      <input type="password" id="re_new_password" class="form__field_blue" placeholder="Powtórz nowe hasło" v-model="re_new_password" required/>
                      <label for="re_new_password" class="form__label_blue">Powtórz nowe hasło</label>
                    </div>
                  </div>
                  <br />
                  <div class="d-grid">
                    <MDBBtn class="btn" rounded type="submit" style="background-color: #add9ee; color: black"><b>Zmień hasło</b></MDBBtn>
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
  data() {
    return {
      uid: this.$route.params.uid,
      token: this.$route.params.token,
      new_password: "",
      re_new_password: "",
      alert: false,
      errors: [],
    };
  },
  components: {
    MDBBtn,
  },
  mounted() {
    document.title = "Zmiana hasła";
    window.scrollTo(0,document.body.scrollHeight);
  },
  methods: {
    async submitForm() {
      this.errors = [];
      this.alert=false;
      if(this.new_password !== this.re_new_password){
        this.errors.push('Hasła do siebie nie pasują')}
if (!this.errors.length) {
      const formData = {
        uid: this.uid,
        token: this.token,
        new_password: this.new_password,
        re_new_password: this.re_new_password,
      };

      await axios
        .post("api/furniture_app/users/reset_password_confirm/", formData)
        .then((response) => {
          //console.log(response);
          this.alert = true;
        })
        .catch((error) => {
          console.log(error);
        });
    }
    },
  },
};
</script>

<style>
/* css do wyglądu inputów*/
.form__group_blue {
  position: relative;
  padding: 15px 0 0;
  margin-top: 10px;
}

.form__field_blue {
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

.form__field_blue::placeholder {
  color: transparent;
}

.form__field_blue:placeholder-shown ~ .form__label {
  font-size: 16px;
  cursor: text;
  top: 20px;
}

label,
.form__field_blue:focus ~ .form__label_blue {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 12px;
  color: #9b9b9b;
}

.form__field_blue:focus ~ .form__label_blue {
  color: #065aa8;
}

.form__field_blue:focus {
  padding-bottom: 6px;
  border-bottom: 2px solid #065aa8;
}
</style>