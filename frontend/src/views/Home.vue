<template>
  <div class="home">
    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to StudyNet!</h1>
        <h2 class="subtitle">A Study Platform!</h2>
      </div>
    </div>

    <section class="section">
      <WelcomeBoxes />
    </section>
  </div>
</template>

<script>
import WelcomeBoxes from "@/components/mainpage/WelcomeBoxes";

export default {
  name: "Home",
  components: {
    WelcomeBoxes,
  },
};
</script>
