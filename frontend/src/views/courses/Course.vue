<template>
    <div class="course">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">{{course.title}}</h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns content">
                    <div class="column is-2">
                        <h2>Content</h2>
                        <ul>
                            <li v-for="lesson in lessons" v-bind:key="lesson.id">
                                <a @click='activeLesson = lesson'>{{lesson.title}}</a>
                            </li>
                        </ul>
                    </div>

                    <div class="column is-10">
                        <template v-if="$store.state.user.isAuthenticated">
                            <template v-if="activeLesson">
                                <h1 class="is-2">{{ activeLesson.title }}</h1>
                                <h4 class="is-4">{{ activeLesson.long_description }}</h4>
                            </template>
                            <template v-else>
                                <h4 class="is-4">{{ course.long_description }}</h4>
                                <template>
                                </template>
                            </template></template>
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
    import axios from 'axios'
    export default {
        name: 'Course',
        data() {
            return {
                course: {},
                lessons: [],
                activeLesson: null
            }
        },
        async mounted() {

            const slug = this.$route.params.slug

            await axios
                .get(`/api/v1/courses/${slug}/`)
                .then(response => {
                    this.course = response.data.course
                    this.lessons = response.data.lessons

                }).catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
</script>