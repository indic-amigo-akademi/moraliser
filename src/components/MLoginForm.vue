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
            <small class="invalid-feedback" v-if="errors.username">{{ errors.username }}</small>
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
            <small class="invalid-feedback" v-if="errors.password">{{ errors.password }}</small>
        </div>
        <div class="btn-container text-center p-4">
            <button type="submit" class="btn btn-success">Login</button>
        </div>
    </form>
</template>

<script lang="js">
import { mapActions } from "vuex";
import { postData } from "@/utils/fetchUtils";

export default {
    name: "m-login-form",
    props: {},
    data() {
        return {
            username: "",
            password: "",
            errors: {
                username: "",
                password: "",
                all: ""
            }
        };
    },
    methods: {
        loginSubmit() {
            postData("/api/login", { username: this.username, password: this.password }, (res) => {
                Object.keys(this.errors).forEach((err) => (this.errors[err] = ""));
                // console.log(res);
                if (res.success) {
                    this.closeLoginModal();
                    window.location.reload();
                } else {
                    Object.keys(res.errors).forEach((err) => (this.errors[err] = res.errors[err].join(" ")));
                }
            });
        },
        ...mapActions(["closeLoginModal"])
    }
};
</script>
