<template>
  <div class="course">
    <div class="hero is-info">
      <div class="hero-body has-text-centered">
        <h1 class="title">{{ course.title }}</h1>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns content">
          <div class="column is-2">
            <h2>Content</h2>
            <ul>
              <li v-for="lesson in lessons" v-bind:key="lesson.id">
                <a @click="setActiveLesson(lesson)">{{ lesson.title }}</a>
              </li>
            </ul>
          </div>

          <div class="column is-10">
            <template v-if="$store.state.user.isAuthenticated">
              <template v-if="activeLesson">
                <h1 class="is-2">{{ activeLesson.title }}</h1>
                <h4 class="is-4">{{ activeLesson.long_description }}</h4>
                <hr />
                <template v-if="activeLesson.lesson_type === 'quiz'">
                  <h3>{{ quiz.question }}</h3>

                  <div class="control">
                    <label class="radio">
                      <input
                        type="radio"
                        :value="quiz.option1"
                        v-model="selectedAnswer"
                      />
                      {{ quiz.option1 }}
                    </label>
                  </div>
                  <div class="control">
                    <label class="radio">
                      <input
                        type="radio"
                        :value="quiz.option2"
                        v-model="selectedAnswer"
                      />
                      {{ quiz.option2 }}
                    </label>
                  </div>
                  <div class="control">
                    <label class="radio">
                      <input
                        type="radio"
                        :value="quiz.option3"
                        v-model="selectedAnswer"
                      />
                      {{ quiz.option3 }}
                    </label>
                  </div>
                  <div class="control">
                    <label class="radio">
                      <input
                        type="radio"
                        :value="quiz.option4"
                        v-model="selectedAnswer"
                      />
                      {{ quiz.option4 }}
                    </label>
                  </div>
                  <div class="control mt-4">
                    <button class="button is-info" @click="submitQuiz">
                      Submit
                    </button>
                  </div>
                </template>

                <template v-if="activeLesson.lesson_type === 'article'">
                  <article
                    class="media box is-info"
                    v-for="comment in comments"
                    v-bind:key="comment.id"
                  >
                    <div class="media-content">
                      <div class="content">
                        <strong>{{ comment.name }} </strong>
                        {{ comment.created_at }} <br />

                        {{ comment.content }}
                      </div>
                    </div>
                  </article>

                  <form @submit.prevent="submitComment()">
                    <div class="field">
                      <label class="label">Name</label>
                      <div class="control">
                        <input
                          type="text"
                          class="input"
                          v-model="comment.name"
                        />
                      </div>
                    </div>
                    <div class="field">
                      <label class="label">Comment</label>
                      <div class="control">
                        <textarea
                          type="textarea"
                          class="textarea"
                          v-model="comment.content"
                        />
                      </div>
                    </div>

                    <div
                      class="notification is-danger"
                      v-for="error in errors"
                      v-bind:key="error"
                    >
                      {{ error }}
                    </div>

                    <div class="field">
                      <div class="control">
                        <button class="button is-link">Leave comment</button>
                      </div>
                    </div>
                  </form>
                </template>
              </template>
            </template>
            <template v-else>
              <h2>Restricted access</h2>
              <p>Please login first</p>
            </template>
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
  name: "Course",
  data() {
    return {
      course: {},
      lessons: [],
      comments: [],
      errors: [],
      activeLesson: null,
      quiz: {},
      selectedAnswer: "",
      quizResult: null,
      comment: {
        name: "",
        content: "",
      },
    };
  },
  async mounted() {
    const slug = this.$route.params.slug;

    await axios
      .get(`/api/v1/courses/${slug}/`)
      .then((response) => {
        this.course = response.data.course;
        this.lessons = response.data.lessons;

        this.setActiveLesson(lessons);
      })
      .catch((error) => {
        console.log(JSON.stringify(error));
      });

    document.title = this.course.title;
  },
  methods: {
    getComments() {
      this.quiz = {};
      axios
        .get(
          `/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/get-comments/`
        )
        .then((response) => {
          this.comments = response.data;
          console.log(this.comments);
        });
    },
    setActiveLesson(lesson) {
      this.activeLesson = lesson;
      if (lesson.lesson_type === "quiz") {
        this.getQuiz();
      } else {
        this.getComments();
      }
    },
    getQuiz() {
      axios
        .get(
          `/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/get-quiz/`
        )
        .then((response) => {
          console.log(response.data);

          this.quiz = response.data;
        });
    },
    submitQuiz() {
      this.quizResult = null;
      this.selectedAnswer
        ? this.selectedAnswer === this.quiz.answer
          ? (this.quizResult = "correct")
          : (this.quizResult = "wrong")
        : toast({
            message: "Select at option first!",
            type: "is-link",
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: "bottom-right",
          });
      toast({
        message: this.quizResult,
        type: "is-link",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });
      console.log(this.quizResult);
    },
    submitComment() {
      this.errors = [];

      if (this.comment.name === "") {
        this.errors.push("the name must be filled.");
      }

      if (this.comment.content.length < 25) {
        this.errors.push("Comment too short..");
      }

      if (!this.errors.length) {
        axios
          .post(
            `/api/v1/courses/${this.course.slug}/${this.activeLesson.slug}/`,
            this.comment
          )
          .then((response) => {
            this.comment.name = "";
            this.comment.content = "";
            this.comments.push(response.data);
            toast({
              message: "Thank you for your feedback!",
              type: "is-link",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>