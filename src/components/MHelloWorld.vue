<template>
    <section class="hello-section p-4 bg-gray-200 rounded-3">
        <div class="container-fluid py-5 text-center">
            <h1>{{ msg }}</h1>
            <p class="lead">A new safe and filtered messaging app.</p>
            <a class="btn btn-primary" data-toggle="modal" data-target="#reglogModal" href="#" role="button">
                Getting Started
            </a>
            <div class="mt-2">&nbsp;</div>
            <router-link class="btn btn-secondary" to="/demo-chat"> See Demo </router-link>
        </div>
    </section>
</template>

<script>
export default {
    name: "m-hello-world",
    props: {
        msg: String
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
