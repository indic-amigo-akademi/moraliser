<template>
  <form class="form loginForm" @submit.prevent="loginSubmit">
    <div class="form-group">
      <label for="lfuser">Username/Email</label>
      <input
        type="text"
        v-model="username"
        name="lfuser"
        id="lfuser"
        class="form-control"
        placeholder="Enter username"
      />
    </div>
    <div class="form-group">
      <label for="lfpwd">Password</label>
      <input
        type="password"
        v-model="password"
        name="lfpwd"
        id="lfpwd"
        class="form-control"
        placeholder="Enter password"
      />
    </div>
    <div class="btn-container text-center">
      <button type="submit" class="btn btn-success">Login</button>
    </div>
  </form>
</template>

<script>
export default {
  name: 'mlogin-form',
  props: {},
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    loginSubmit () {
      const data = new FormData()
      data.append('username', this.username)
      data.append('password', this.password)

      fetch(`http://${location.hostname}:${location.port}/api/login`, {
        method: 'POST',
        body: data
      })
        .then((res) => {
          if (res.status !== 200) { throw Error(res.statusText) }
          return res.json()
        })
        .then((msg) => {
          console.log(msg)
        })
        .catch((err) => {
          console.error(err)
        })
    }
  }
}
</script>
