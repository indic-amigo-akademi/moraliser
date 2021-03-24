<template>
  <div class="hello jumbotron">
    <h1>{{ msg }}</h1>
    <p class="lead">A new safe and filtered messaging app.</p>
    <a
      class="btn btn-primary"
      data-toggle="modal"
      data-target="#reglogModal"
      href="#"
      role="button"
    >
      Getting Started
    </a>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.hello {
  margin: 5rem 0;
  text-align: center;
}
</style>
