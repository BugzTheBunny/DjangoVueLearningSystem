<template>
  <div>
    <Navbar />
    <router-view />

    <Footer />
  </div>
</template>

<script>
import axios from "axios";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
export default {
  name: "App",
  components: {
    Navbar,
    Footer,
  },
  beforeCreate() {
    this.$store.commit("initializeStore");

    const token = this.$store.state.user.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";

.navbar {
  min-height: 5rem;
  background: #4267b2;
}

/*Welcome Page*/
.welcome-box {
  transition: transform 0.5s;
}

.welcome-box:hover {
  transform: scale(1.1);
}

.is-start-btn {
  background: #4267b2;
  color: white;
  transition: transform 0.5s;
}
.is-start-btn:hover {
  color: white;
  transform: scale(1.1);
}
</style>
