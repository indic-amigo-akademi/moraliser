<template>
  <form class="form login-form" @submit.prevent="loginSubmit">
    <small class="invalid-feedback" v-if="errors.all">{{ errors.all }}</small>
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
      <small class="invalid-feedback" v-if="errors.username">{{
        errors.username
      }}</small>
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
      <small class="invalid-feedback" v-if="errors.password">{{
        errors.password
      }}</small>
    </div>
    <div class="btn-container text-center p-4">
      <button type="submit" class="btn btn-success">Login</button>
    </div>
  </form>
</template>

<script lang="ts">
import { mapActions } from "vuex";
import {
  postData,
  redirectTo,
  type FetchResponseJSON,
} from "@/utils/fetchUtils";
import { updateCurrentUser } from "@/utils/authUtils";

export default {
  name: "m-login-form",
  data() {
    return {
      username: "",
      password: "",
      errors: {
        username: "",
        password: "",
        all: "",
      },
    };
  },
  methods: {
    loginSubmit() {
      type FetchReqType = { [key: string]: { [key: string]: string[] } };
      postData<FetchReqType>(
        "/api/login",
        { username: this.username, password: this.password },
        (res: FetchResponseJSON<FetchReqType>) => {
          (Object.keys(this.errors) as (keyof typeof this.errors)[]).forEach(
            (key) => (this.errors[key] = "")
          );
          if (res.success) {
            this.closeLoginModal();
            redirectTo("chat");
            updateCurrentUser();
          } else {
            console.log(res);
            (
              Object.keys(res.data.errors) as (keyof typeof this.errors)[]
            ).forEach(
              (key) => (this.errors[key] = res.data.errors[key].join(" "))
            );
          }
        }
      );
    },
    ...mapActions(["closeLoginModal"]),
  },
};
</script>
