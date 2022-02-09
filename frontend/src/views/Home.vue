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
      <hr />
      <div class="column is-12">
        <div class="columns is-multiline">
          <div
            class="column is-3"
            v-for="course in courses"
            v-bind:key="course.id"
          >
            <CourseItem :course="course" />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import WelcomeBoxes from "@/components/mainpage/WelcomeBoxes";
import axios from "axios";
import CourseItem from "@/components/courses/CourseItem";

export default {
  name: "Home",
  data() {
    return {
      courses: [],
    };
  },
  components: {
    WelcomeBoxes,
    CourseItem,
  },
  async mounted() {
    await axios
      .get("/api/v1/courses/get_frontpage_courses/")
      .then((response) => {
        this.courses = response.data;
      })
      .then({})
      .catch((error) => {
        console.log(JSON.stringify(error));
      });
    document.title = "StudyNet | Home";
  },
};
</script>
