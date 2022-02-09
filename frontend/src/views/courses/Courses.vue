<template>
  <div class="courses">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">Courses</h1>
      </div>
    </div>
    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-2">
            <aside class="menu">
              <p class="menu-label">Categories</p>

              <ul class="menu-list">
                <li>
                  <!-- Will show is-active if no category selected. -->
                  <a
                    v-bind:class="{ 'is-active': !activeCategory }"
                    @click="setActiveCategory(null)"
                  >
                    All Courses</a
                  >
                </li>
                <li
                  v-for="category in categories"
                  v-bind:key="category.id"
                  @click="setActiveCategory(category)"
                >
                  <a>{{ category.title }}</a>
                </li>
              </ul>
            </aside>
          </div>
          <div class="column is-10">
            <div class="columns is-multiline">
              <div
                class="column is-4"
                v-for="course in courses"
                v-bind:key="course.id"
              >
                <CourseItem :course="course" />
              </div>
            </div>
          </div>
        </div>
        <hr />
        <div class="column is-12">
          <nav class="pagination">
            <a href="#" class="pagination-previous">Previous</a>
            <a href="#" class="pagination-next">Next</a>
            <ul class="pagination-list">
              <li>
                <a href="" class="pagination-link is-current">1</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import CourseItem from "@/components/courses/CourseItem";
export default {
  name: "Courses",
  data() {
    return {
      courses: [],
      categories: [],
      activeCategory: null,
    };
  },
  components: {
    CourseItem,
  },
  async mounted() {
    await axios.get("/api/v1/courses/get_categories/").then((response) => {
      this.categories = response.data;
    });

    this.getCourses();
    document.title = "Courses";
  },
  methods: {
    setActiveCategory(category) {
      this.activeCategory = category;

      this.getCourses();
    },

    getCourses() {
      let url = "/api/v1/courses/";

      if (this.activeCategory) {
        url += `?category_id=${this.activeCategory.id}`;
      }

      axios.get(url).then((response) => {
        this.courses = response.data;
      });
    },
  },
};
</script>