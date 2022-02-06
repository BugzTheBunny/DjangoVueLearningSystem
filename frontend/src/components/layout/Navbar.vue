<template>
  <nav
    class="navbar is-transparent"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="navbar-brand">
      <a href="/" class="navbar-item is-size-4 has-text-white"
        ><strong>StudyNet</strong></a
      >
    </div>
    <div class="navbar-menu" id="navbar-item">
      <div class="navbar-start">
        <router-link
          :to="{ name: 'Courses' }"
          class="navbar-item has-text-white"
        >
          Courses</router-link
        >
      </div>
      <div class="navbar-end">
        <template v-if="!$store.state.user.isAuthenticated">
          <div class="navbar-item">
            <div class="buttons">
              <router-link
                :to="{ name: 'SignUp' }"
                class="button is-dark has-text-white"
                >Sign up</router-link
              >
              <router-link
                :to="{ name: 'LogIn' }"
                class="button is-dark has-text-white"
                >Log in</router-link
              >
            </div>
          </div>
        </template>
        <template v-else>
          <div class="navbar-item">
            <router-link :to="{ name: 'MyAccount' }" class="has-text-white"
              >My Account</router-link
            >
          </div>
        </template>
      </div>
    </div>
  </nav>
</template>

<script>
import axios from "axios";
export default {
  name: "Navbar",
  methods: {},
};
</script>