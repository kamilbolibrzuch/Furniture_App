<template>
    <div class="container-fluid ps-md-0">
        <div class="row g-0">
            <div class="d-none d-md-flex col-md-4 col-lg-6 bg-image2"></div>
            <div class="col-md-8 col-lg-6">
            <div class="login d-flex align-items-center py-5">
                <div class="container">
                <div class="row">
                    <div class="col-md-9 col-lg-8 mx-auto">
                    <h3 class="login-heading mb-4" style="font-family: 'Libre Baskerville', serif; font-size: 250%;">Rejestracja</h3>

                    <!-- Formularz rejestracji -->
                    <form @submit.prevent="submitForm">
                        <div class="form-floating mb-3">
                            <div class="form__group">
                                <input type="text" id="username" class="form__field" placeholder="Nazwa użytkownika" v-model="username" required >
                                <label for="username" class="form__label">Nazwa użytkownika</label>
                            </div>
                        </div>

                        <div class="form-floating mb-3">
                            <div class="form__group">
                                <input type="text" id="email" class="form__field" placeholder="email" v-model="email" required >
                                <label for="email" class="form__label">E-mail</label>
                            </div>
                        </div>

                        <div class="form-floating mb-3">
                            <div class="form__group">
                                <input type="password" id="password" class="form__field" placeholder="Hasło" v-model="password" required >
                                <label for="password" class="form__label">Hasło</label>
                            </div>
                        </div>

                        <div class="form-floating mb-3">
                            <div class="form__group">
                                <input type="password" id="password2" class="form__field" placeholder="Hasło" v-model="password2" required >
                                <label for="password2" class="form__label">Powtórz swoje hasło</label>
                            </div>
                        </div>
                           <br>
                        <div class="d-grid">
                        <MDBBtn  class=" btn btn-lg" rounded type="submit" style="background-color:#004D40; color:white;">Zarejestruj się</MDBBtn>
                        <div class="text-center">
                            <br>
                 Masz konto?<router-link to="/log-in" style="color: #009788;"> Zaloguj się</router-link> 
                        </div>
                        
                     <!-- Alerty -->     
                        <div class="alert alert-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
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
import axios from 'axios'

import { MDBBtn } from "mdb-vue-ui-kit"; 

export default {

    name: 'SignUp',
    components: {
        MDBBtn  
    },
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            email: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Rejestracja'
    },
    methods: {
        submitForm() {
            this.errors = []
            if (this.username === '') {
                this.errors.push('Nie podano nazwy użytkownika').bold()
            }
            if (this.password === '') {
                this.errors.push('Hasło jest za krótkie')
            }
            if (this.password !== this.password2) {
                this.errors.push('Hasła do siebie nie pasują')
            }
            if (this.email === '') {
                this.errors.push('Nie podano ardesu e-mail')
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password,
                    email: this.email
                }
                axios
                    .post("/api/furniture_app/users/", formData) 
                    .then(response => {
                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Ups coś poszło nie tak. Spróbuj ponownie')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
            
        }
    }
}
</script>

<style>
.bg-image2 {
  
  background-size: cover;
  background-position: center;
  background-color: #00BCD4;
}
</style>

