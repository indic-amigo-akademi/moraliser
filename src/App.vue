<template>
  <div id="app">
    <mheader></mheader>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
import MHeader from './components/MHeader'

export default {
  name: 'app',
  components: {
    mheader: MHeader
  }
}
</script>

<style lang="scss">
body,
#app {
  display: flex;
  width: 100%;
  height: 100vh;
  flex-direction: column;
}

main {
  padding: 0;
  -webkit-box-flex: 1;
  -ms-flex: 1 0 auto;
  flex: 1 0 auto;
  overflow: hidden;
}

header,
footer {
  flex-shrink: 0;
  border-radius: 0px;
}
</style>
