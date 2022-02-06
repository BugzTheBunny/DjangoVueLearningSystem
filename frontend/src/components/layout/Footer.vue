<template>
  <footer class="footer">
    <p class="has-text-centered">Copyrights (c) 2022</p>
    <p class="has-text-centered">
      <router-link :to="{ name: 'About' }">About</router-link>
    </p>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  methods: {},
};
</script>