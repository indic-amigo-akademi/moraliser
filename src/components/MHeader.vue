<template>
  <header>
    <nav class="navbar navbar-expand-md navbar-light bg-light">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <router-link class="navbar-brand" to="/">
          <img :src="logo" width="30" height="30" alt="" loading="lazy">
      </router-link>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item active">
            <router-link to="/">Home</router-link>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
import logo from '@/assets/logo.png'

export default {
  name: 'mheader',
  created () {},
  data () {
    return {
      logo: logo
    }
  },
  props: {},
  methods: {}
}
</script>

<style lang="scss" scoped></style>
