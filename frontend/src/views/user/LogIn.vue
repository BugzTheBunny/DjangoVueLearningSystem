<template>
  <div class="login">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Log In</h1>
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
                  <input type="email" class="input" v-model="username" />
                </div>
              </div>
              <div class="field">
                <label>Password</label>
                <div class="control">
                  <input type="password" class="input" v-model="password" />
                </div>
              </div>
              <div class="notification is-danger" v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error">
                  {{ error }}
                </p>
              </div>
              <div class="field">
                <div class="control">
                  <button class="button is-dark is-fullwidth">Log In</button>
                </div>
              </div>
            </form>
            <hr />
            <div class="container has-text-centered">
              Don't have an account?
              <router-link :to="{ name: 'SignUp' }"
                ><strong> Register here</strong></router-link
              >
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "LogIn",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "StudyNet | Log In";
  },
  methods: {
    async submitForm() {
      this.errors = [];

      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");

      if (this.username === "") {
        this.errors.push("Please enter an email");
      }
      if (this.password === "") {
        this.errors.push("Password missing");
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };

        await axios
          .post("/api/v1/token/login/", formData)
          .then((response) => {
            const token = response.data.auth_token;

            this.$store.commit("setToken", token);

            axios.defaults.headers.common["Authorization"] = "Token " + token;

            localStorage.setItem("token", token);

            this.$router.push({ name: "MyAccount" });

            toast({
              message: "Welcome!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}:${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong.");
              console.log(JSON.stringify(error));
            }
          });
      }
    },
  },
};
</script>