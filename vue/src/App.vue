<template>
  <div id="app">
    <h1>Top Questions</h1>
    <div v-for="question in questionList" :key="question.id">
      <question-item :initialData="question"></question-item>
    </div>
  </div>

  <router-view />
</template>

<script>
import axios from 'axios';
import QuestionItem from './components/QuestionItem.vue';

export default {
  name: 'App',
  components: {
    QuestionItem,
  },
  data () {
    return {
      questionList: [],
    }
  },
  mounted () {
    axios
      .get('http://127.0.0.1:8000/')
      .then(response => {
        console.log(response);
        this.questionList = response.data;
        })
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
