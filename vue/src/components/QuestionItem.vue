<template>
  <div class="question-summary">
    <div>
      <div>
        <div>
          <a>{{ votes }} {{ votes==1 ? "Vote":"Votes" }}</a>
          <button @click="upvote">+</button>
        </div>
        <div><a>{{ answer_count }} {{ answer_count==1 ? "Answer":"Answers" }}</a></div>
        <div><a>{{ views }} {{ views==1 ? "View":"Views" }}</a></div>
      </div>
      <div>
        <div>
          <p>{{ title }}</p>
        </div>
        <div v-for="tag in tags" :key="tag"><a>{{ tag }}</a></div>
        <div><a>{{ timestamp }}</a></div>
        <div><a>{{ author }}</a></div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'QuestionItem',
  props: ['initialData'],
  data () {
    console.log(this.initialData);
    return {...this.initialData};
  },
  computed: {
  },
  methods: {
    upvote(){
      this.votes += 1;
    }
  }
};
</script>
