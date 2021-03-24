<template>
  <form class="form registerForm" @submit.prevent="registerSubmit">
    <div class="form-group">
      <label for="rfuser">Email</label>
      <input
        type="email"
        v-model="email"
        name="rfemail"
        id="rfemail"
        class="form-control"
        placeholder="Enter email"
      />
    </div>
    <div class="form-group">
      <label for="rfuser">Username</label>
      <input
        type="text"
        v-model="username"
        name="rfuser"
        id="rfuser"
        class="form-control"
        placeholder="Enter username"
      />
    </div>
    <div class="form-group">
      <label for="rfpwd">Password</label>
      <input
        type="text"
        v-model="password"
        name="rfpwd"
        id="rfpwd"
        class="form-control"
        placeholder="Enter password"
      />
    </div>
    <div class="form-group">
      <label for="rfpwd">Repeat Password</label>
      <input
        type="text"
        v-model="rpassword"
        name="rfrpwd"
        id="rfrpwd"
        class="form-control"
        placeholder="Confirm password"
      />
    </div>
    <div class="btn-container text-center">
      <button type="submit" class="btn btn-success">Register</button>
    </div>
  </form>
</template>

<script>
export default {
  name: 'mregister-form',
  props: {},
  data () {
    return {
      email: '',
      username: '',
      password: '',
      rpassword: ''
    }
  },
  methods: {
    registerSubmit () {
      if (this.password !== this.rpassword) {
        console.log('Passwords do not match')
        return
      }

      const data = new FormData()
      data.append('email', this.email)
      data.append('username', this.username)
      data.append('password', this.password)

      fetch(`http://${location.hostname}:${location.port}/#/api/register`, {
        method: 'POST',
        body: data
      })
        .then((res) => res.json())
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
