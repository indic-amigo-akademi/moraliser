<script setup lang="ts">
import { reactive } from "vue";
import { useStore } from "vuex";
import {
    postData,
    redirectTo,
    type FetchResponseJSON,
} from "@/utils/fetchUtils";
import { updateCurrentUser } from "@/utils/authUtils";
import MFormInput from "@/atoms/MFormInput/MFormInput.vue";

const state = reactive(
    {
        username: "",
        password: "",
        errors: {
            username: "",
            password: "",
            all: "",
        },
    }
);

const store = useStore();

function closeLoginModal() {
    store.dispatch("closeLoginModal");
}

function loginSubmit() {
    type FetchReqType = { [key: string]: { [key: string]: string[] } };
    postData<FetchReqType>(
        "/api/login",
        { username: state.username, password: state.password },
        (res: FetchResponseJSON<FetchReqType>) => {
            (Object.keys(state.errors) as (keyof typeof state.errors)[]).forEach(
                (key) => (state.errors[key] = "")
            );
            if (res.success) {
                closeLoginModal();
                redirectTo("chat");
                updateCurrentUser();
            } else {
                console.log(res);
                (
                    Object.keys(res.data.errors) as (keyof typeof state.errors)[]
                ).forEach(
                    (key) => (state.errors[key] = res.data.errors[key].join(" "))
                );
            }
        }
    );
}
</script>


<template>
    <form class="form login-form" @submit.prevent="loginSubmit">
        <small class="invalid-feedback" v-if="state.errors.all">{{ state.errors.all }}</small>

        <m-form-input label="Username/Email" prepend-icon="carbon:user-avatar" placeholder="Enter username"
            rule="required,email,min:3" v-model="state.username" name="username" />

        <m-form-input label="Password" input-type="password" prepend-icon="carbon:password" placeholder="Enter password"
            rule="required,min:8" v-model="state.password" name="password" />

        <div class="btn-container text-center p-4">
            <button type="submit" class="btn btn-success">Login</button>
        </div>
    </form>
</template>
