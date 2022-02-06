<template>
  <div class="login">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome!</h1>
        <button class="button is-primary" @click="logout()">
          <strong>Log out</strong>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MyAccount",
  methods: {
    async logout() {
      await axios
        .post("/api/v1/token/logout/")
        .then((response) => {})
        .catch((error) => {
          console.log(JSON.stringify(error));
        });

      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");

      this.$store.commit("removeToken");

      this.$router.push({ name: "LogIn" });
    },
  },
};
</script>