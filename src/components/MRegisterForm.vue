<template>
    <form class="form registerForm" @submit.prevent="registerSubmit">
        <div class="form-group">
            <label for="rfemaill">Email</label>
            <input
                type="email"
                v-model="email"
                name="rfemail"
                id="rfemail"
                class="form-control"
                autocomplete="email"
                :class="{ 'is-invalid': errors.email, 'is-valid': !errors.email }"
                placeholder="Enter email"
            />
            <small class="invalid-feedback" v-if="errors.email">{{ errors.email }}</small>
        </div>
        <div class="form-group">
            <label for="rfuser">Username</label>
            <input
                type="text"
                v-model="username"
                name="rfuser"
                id="rfuser"
                class="form-control"
                autocomplete="username"
                :class="{ 'is-invalid': errors.username, 'is-valid': !errors.username }"
                placeholder="Enter username"
            />
            <small class="invalid-feedback" v-if="errors.username">{{ errors.username }}</small>
        </div>
        <div class="form-group">
            <label for="rfphone">Phone</label>
            <input
                type="text"
                v-model="phone"
                name="rfphone"
                id="rfphone"
                class="form-control"
                autocomplete="tel"
                :class="{ 'is-invalid': errors.phone, 'is-valid': !errors.phone }"
                placeholder="Enter mobile number"
            />
            <small class="invalid-feedback" v-if="errors.phone">{{ errors.phone }}</small>
        </div>
        <div class="form-group">
            <label for="rfpwd">Password</label>
            <input
                type="password"
                v-model="password"
                name="rfpwd"
                id="rfpwd"
                class="form-control"
                autocomplete="new-password"
                :class="{ 'is-invalid': errors.password, 'is-valid': !errors.password }"
                placeholder="Enter password"
            />
            <small class="invalid-feedback" v-if="errors.password">{{ errors.password }}</small>
        </div>
        <div class="form-group">
            <label for="rfpwd">Repeat Password</label>
            <input
                type="password"
                v-model="rpassword"
                name="rfrpwd"
                id="rfrpwd"
                class="form-control"
                autocomplete="new-password"
                :class="{ 'is-invalid': errors.rpassword, 'is-valid': !errors.rpassword }"
                placeholder="Confirm password"
            />
            <small class="invalid-feedback" v-if="errors.rpassword">{{ errors.rpassword }}</small>
        </div>
        <div class="btn-container text-center p-4">
            <button type="submit" class="btn btn-success">Register</button>
        </div>
    </form>
</template>

<script>
import { mapActions } from "vuex";

export default {
    name: "m-register-form",
    props: {},
    data() {
        return {
            email: "",
            username: "",
            phone: "",
            password: "",
            rpassword: "",
            errors: {
                email: "",
                username: "",
                phone: "",
                password: "",
                rpassword: ""
            }
        };
    },
    methods: {
        registerSubmit() {
            if (this.password !== this.rpassword) {
                this.rpassword = "Passwords do not match";
                return;
            }

            const data = new FormData();

            data.append("csrf_token", document.querySelector("meta[name='csrf_token']").getAttribute("content"));
            data.append("email", this.email);
            data.append("phone", this.phone);
            data.append("username", this.username);
            data.append("password", this.password);

            fetch(`http://${location.hostname}:${location.port}/api/register`, {
                method: "POST",
                body: data
            })
                .then((res) => {
                    if (res.status !== 200) {
                        throw Error(res.statusText);
                    }
                    return res.json();
                })
                .then((res) => {
                    Object.keys(this.errors).forEach((err) => (this.errors[err] = ""));
                    if (res.success) {
                        this.closeLoginModal();
                        window.location.reload();
                    } else {
                        Object.keys(res.errors).forEach((err) => (this.errors[err] = res.errors[err].join(" ")));
                    }
                    // console.log(res.message);
                })
                .catch((err) => {
                    console.error(err);
                });
        },
        ...mapActions(["closeLoginModal"])
    }
};
</script>
