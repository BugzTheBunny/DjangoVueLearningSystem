<template>
  <div class="card">
    <div class="card-image">
      <figure class="image is-4by3">
        <img :src="course.get_image" alt="course-image" />
      </figure>
    </div>
    <div class="card-content">
      <div class="media">
        <div class="media-content">
          <p class="is-size-5">{{ course.title }}</p>
        </div>
      </div>
      <div class="content">
        <p>{{ course.slug }} | {{ course.short_description }}</p>
        <router-link
          :to="{ name: 'Course', params: { slug: course.slug } }"
          class="button is-fullwidth is-primary"
          >View
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CourseItem",
  props: ["course"],
};
</script>