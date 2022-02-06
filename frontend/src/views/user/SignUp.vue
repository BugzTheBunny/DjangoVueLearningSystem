<template>
    <div class="signup">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">
                    Sign Up
                </h1>
            </div>
        </div>
        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="box column is-4 is-offset-4">
                        <form @submit.prevent="submitForm">
                            <div class="field">
                                <label>Email</label>
                                <div class="control">
                                    <input type="email" class="input" v-model="username">
                                </div>
                            </div>
                            <div class="field">
                                <label>Password</label>
                                <div class="control">
                                    <input type="password" class="input" v-model="password1">
                                </div>
                            </div>
                            <div class="field">
                                <label>Confirm password</label>
                                <div class="control">
                                    <input type="password" class="input" v-model="password2">
                                </div>
                            </div>
                            <div class="container has-text-centered">
                                Or <router-link :to="{ name: 'LogIn' }"><strong>Click here</strong></router-link> to log
                                in
                            </div>
                            <div class="field">
                                <div class="control">
                                    <button class="button is-dark is-fullwidth">Sign Up</button>
                                </div>
                            </div>
                        </form>
                        <hr>
                        <div class="notification is-danger" v-if="errors.length">
                            <p v-for="error in errors" v-bind:key="error">
                                {{error}}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    import axios from 'axios'
    import { toast } from 'bulma-toast'

    export default {
        name: 'SignUp',
        data() {
            return {
                username: '',
                password1: '',
                password2: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                console.log('Submit')

                this.errors = []

                if (this.username === "") {
                    this.errors.push('Please enter an email')
                }
                if (this.password1 === "" | this.password2 === "") {
                    this.errors.push('Password missing')
                }
                if (this.password1 != this.password2) {
                    this.errors.push("Passwords don't match")
                }

                if (!this.errors.length) {
                    const formData = {
                        username: this.username,
                        password: this.password1
                    }

                    await axios
                        .post('/api/v1/users/', formData)
                        .then(response => {
                            toast({
                                message: "Account was created, please log in",
                                type: "is-success",
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: "bottom-right",
                            });
                            this.$router.push({ name: 'LogIn' })
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response.data) {
                                    this.errors.push(`${property}:${error.response.data[property]}`)
                                }

                                console.log(JSON.stringify(error.response.data))
                            } else if (error.message) {
                                this.errors.push('Something went wrong.')
                                console.log(JSON.stringify(error))
                            }
                        })
                }

            },
        }
    }
</script>