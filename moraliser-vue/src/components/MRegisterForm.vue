<script setup lang="ts">
import { useStore } from "vuex";
import { postData, type FetchResponseJSON } from "@/utils/fetchUtils";
import { reactive } from "vue";
import MFormInput from "@/atoms/MFormInput/MFormInput.vue";

const state = reactive({
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
        rpassword: "",
    },
});

const registerSubmit = () => {
    if (state.password !== state.rpassword) {
        state.rpassword = "Passwords do not match";
        return;
    }

    type FetchReqType = { [key: string]: { [key: string]: string[] } };
    postData<FetchReqType>(
        "/api/register",
        {
            email: state.email,
            phone: state.phone,
            username: state.username,
            password: state.password,
        },
        (res: FetchResponseJSON<FetchReqType>) => {
            (Object.keys(state.errors) as (keyof typeof state.errors)[]).forEach(
                (key) => (state.errors[key] = "")
            );
            if (res.success) {
                closeLoginModal();
                window.location.reload();
            } else {
                console.log(res.message);
                (
                    Object.keys(res.data.errors) as (keyof typeof state.errors)[]
                ).forEach(
                    (key) => (state.errors[key] = res.data.errors[key].join(" "))
                );
            }
        }
    );
};

const store = useStore();

const closeLoginModal = () => store.dispatch("closeLoginModal");
</script>


<template>
    <form class="form registerForm" @submit.prevent="registerSubmit">
        <!-- Email Field -->
        <m-form-input label="Email" prepend-icon="carbon:email" type="email" v-model="state.email"
            v-model:error-value="state.errors.email" placeholder="Enter email" autocomplete="email" name="email"
            rule="required,email" />

        <!-- Username Field -->
        <m-form-input label="Username" prepend-icon="carbon:user" type="text" v-model="state.username"
            v-model:error-value="state.errors.username" placeholder="Enter username" autocomplete="username"
            name="username" rule="required,min:3,max:15" />

        <!-- Phone Field -->
        <m-form-input label="Phone" prepend-icon="carbon:phone" type="phone" v-model="state.phone"
            v-model:error-value="state.errors.phone" placeholder="Enter mobile number" autocomplete="tel"
            name="phone" rule="required,phone" />

        <!-- Password Field -->
        <m-form-input label="Password" prepend-icon="carbon:password" type="password" v-model="state.password"
            v-model:error-value="state.errors.password" placeholder="Enter password" autocomplete="new-password"
            name="password" rule="required,min:6,max:15" />

        <!-- Repeat Password Field -->
        <m-form-input label="Repeat Password" prepend-icon="carbon:password" type="password" v-model="state.rpassword"
            v-model:error-value="state.errors.rpassword" placeholder="Confirm password" autocomplete="new-password"
            name="rfrpwd" rule="required,min:6,max:15,same:password" />

        <div class="btn-container text-center p-4">
            <button type="submit" class="btn btn-success">Register</button>
        </div>
    </form>
</template>
