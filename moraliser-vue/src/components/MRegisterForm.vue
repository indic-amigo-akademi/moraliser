<script setup lang="ts">
import { useStore } from "vuex";
import { postData, type FetchResponseJSON } from "@/utils/fetchUtils";
import { reactive, useTemplateRef } from "vue";
import MFormInput from "@/atoms/MForm/MFormInput.vue";
import MForm from "@/atoms/MForm/MForm.vue";

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

const emailRef = useTemplateRef("email");
const usernameRef = useTemplateRef("username");
const phoneRef = useTemplateRef("phone");
const passwordRef = useTemplateRef("password");
// const rpasswordRef = useTemplateRef("rpassword");

const formRefs = [emailRef, usernameRef, phoneRef, passwordRef];


const registerSubmit = () => {
    if (state.password !== state.rpassword) {
        state.errors.rpassword = "Passwords do not match";
        return;
    }

    const hasErrors = formRefs.some((ref: any) =>
        !ref.value.validate()
    );
    if (hasErrors) return;

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
    <m-form class="registerForm" @submit="registerSubmit">
        <!-- Email Field -->
        <m-form-input label="Email" prepend-icon="carbon:email" input-type="email" v-model="state.email"
            v-model:error-value="state.errors.email" placeholder="Enter email" autocomplete="email" name="email"
            rule="required,email" title="Email" ref="email" container-classname="mb-3" />

        <!-- Username Field -->
        <m-form-input label="Username" prepend-icon="carbon:user" input-type="text" v-model="state.username"
            v-model:error-value="state.errors.username" placeholder="Enter username" autocomplete="username"
            name="username" rule="required,min:3,max:15" title="Username" ref="username" container-classname="mb-3" />

        <!-- Phone Field -->
        <m-form-input label="Phone" prepend-icon="carbon:phone" input-type="phone" v-model="state.phone"
            v-model:error-value="state.errors.phone" placeholder="Enter mobile number" autocomplete="tel" name="phone"
            rule="required,phone" title="Phone Number" ref="phone" container-classname="mb-3" />

        <!-- Password Field -->
        <m-form-input label="Password" prepend-icon="carbon:password" input-type="password" v-model="state.password"
            v-model:error-value="state.errors.password" placeholder="Enter password" autocomplete="new-password"
            name="password" rule="required,min:6,max:15" title="Password" ref="password" container-classname="mb-3" />

        <!-- Repeat Password Field -->
        <m-form-input label="Repeat Password" prepend-icon="carbon:password" input-type="password"
            v-model="state.rpassword" v-model:error-value="state.errors.rpassword" placeholder="Confirm password"
            autocomplete="new-password" name="rfrpwd" rule="required,min:6,max:15,same:password" title="Repeat Password"
            container-classname="mb-3" />

        <div class="btn-container text-center p-4">
            <button type="submit" class="btn btn-success">Register</button>
        </div>
    </m-form>
</template>
