<template>
  <div class="container-fluid ps-md-0">
    <div class="row g-0">
      <div class="d-none d-md-flex col-md-4 col-lg-6" id="bg-image"></div>
      <div class="col-md-8 col-lg-6">
        <div class="login d-flex align-items-center py-5">
          <div class="container">
            <div class="row">
              <div class="col-md-9 col-lg-8 mx-auto">
                <h3 class="login-heading mb-4" style=" font-family: 'Libre Baskerville', serif; font-size: 250%; ">
                  Logowanie
                </h3>

                <!-- Formularz logowania -->
                <form @submit.prevent="submitForm">
                  <div class="form-floating mb-3">
                    <div class="form__group">
                      <input type="text" id="username" class="form__field" placeholder="Nazwa użytkownika" v-model="username" required />
                      <label for="username" class="form__label" >Nazwa użytkownika</label>
                    </div>
                  </div>

                  <div class="form-floating mb-3">
                    <div class="form__group">
                      <input type="password" id="password" class="form__field" placeholder="Hasło" v-model="password" required />
                      <label for="password" class="form__label">Hasło</label>
                    </div>
                  </div>

                  <div class="text-right">
                    <a class="small" href="/password/forgot" style="color: #009788" >Zapomniałeś hasła?</a >
                    <br /><br />
                  </div>

                  <div class="d-grid">
                    <MDBBtn class="btn btn-lg" rounded type="submit" style="background-color: #004d40; color: white" >Zaloguj się</MDBBtn >
                    <div class="text-center">
                      <br />
                      Nie masz jeszcze konta?
                      <router-link to="/sign-up" style="color: #009788"> Zarejestruj się</router-link>
                    </div>

                    <!-- Alerty -->
                    <div class="alert alert-danger" v-if="errors.length">
                      <p v-for="error in errors" v-bind:key="error">
                        {{ error }}
                      </p>
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
      username: "",
      password: "",
      errors: [],
      token: "",
    };
  },

  mounted() {
    document.title = "Logowanie";
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = ""; //resetowanie
      localStorage.removeItem("token"); //resetowanie cd ..
      const formData = {
        username: this.username,
        password: this.password,
      };

      await axios
        .post("/api/furniture_app/token/login/", formData)

        .then((response) => {
          // const token = response.data.auth_token                                      //odbieramy token z serwera
          this.token = response.data.auth_token;
          this.$store.commit("setToken", this.token); //uruchamiamy metodę ze store o nazwie settoken i przekazujemy do niej token

          this.$store.commit("setUserName", this.username); //uruchamiamy metodę ze store o nazwie setUserName i przekazujemy do niej nazwe użytkownika

          axios.defaults.headers.common["Authorization"] =
            "Token " + this.token;

          localStorage.setItem("token", this.token); //zapisujemy token w sesji

          localStorage.setItem("username", this.username);
          
          
          axios
            .get("/api/furniture_app/users/me", {          //gdy mamy już token i jesteśmy uthentykowani to wysyłamy zapytanie o zwórcenie danych zalogowanego usera
              headers: {
                Authorization: `Token ${this.token}`,           //przypisujemy token zwrócony przez djoser
              },
            })
            .then((res) => {
                this.$store.commit("setUserId", res.data.id); //uruchamiamy metodę ze store o nazwie setUserName i przekazujemy do niej nazwe użytkownika
                localStorage.setItem("id", res.data.id); //zapisujemy token w sesji
              
               //this.$router.push('/') 
               window.location.href = "/" // po zalogowaniu i przypisaniu jeśli wszystko się udało przenosimy na strone dashboard
            })
            .catch((error) => {
              console.log(error);
            }); 
        })
        .catch((error) => {
          //jeśli mamy error
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${error.response.data[property]}`); //doddajemy do tablicy błędów
            }
          } else {
            this.errors.push("Ups coś poszło nie tak. Spróbuj ponownie");

            console.log(JSON.stringify(error));
          }
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
