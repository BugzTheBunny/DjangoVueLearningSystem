<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-4 welcome-box">
        <div class="box has-text-centered">
          <span class="icon is-size-2 has-text-info">
            <i class="far fa-clock"></i>
          </span>
          <h2 class="is-size-4 mt-4 mb-4">Study at your own pace</h2>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit,
            maiores.
          </p>
        </div>
      </div>
      <div class="column is-4 welcome-box">
        <div class="box has-text-centered">
          <span class="icon is-size-2 has-text-info">
            <i class="far fa-clock"></i>
          </span>
          <h2 class="is-size-4 mt-4 mb-4">Study from home!</h2>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit,
            maiores.
          </p>
        </div>
      </div>
      <div class="column is-4 welcome-box">
        <div class="box has-text-centered">
          <span class="icon is-size-2 has-text-info">
            <i class="far fa-clock"></i>
          </span>
          <h2 class="is-size-4 mt-4 mb-4">Study for free!</h2>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit,
            maiores.
          </p>
        </div>
      </div>
      <div class="column is-12 has-text-centered">
        <router-link
          :to="{ name: 'SignUp' }"
          class="button is-start-btn is-size-3 mt-6 mb-6"
        >
          Click here to start</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "WelcomeBoxes",
};
</script>