<template>
    <header>
        <nav class="navbar navbar-expand-md navbar-light bg-light">
            <div class="container-fluid">
                <button
                    class="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarNav"
                    aria-controls="navbarNav"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span class="navbar-toggler-icon"></span>
                </button>
                <router-link class="navbar-brand" to="/">
                    <img :src="logo" width="30" height="30" alt="" loading="lazy" />
                </router-link>

                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto">
                        <li class="nav-item">
                            <router-link class="nav-link" active-class="active" to="/">Home</router-link>
                        </li>
                        <li class="nav-item" v-if="isLoggedIn">
                            <a class="nav-link" href="#" @click.prevent="logoutUser">Logout</a>
                        </li>
                        <li class="nav-item" v-else>
                            <a class="nav-link" href="#" @click.prevent="openLoginModal">Login/Register</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
</template>

<script>
import logo from "@/assets/logo.png";
import { mapActions, mapState } from "vuex";
import { postData } from "@/utils/fetchUtils";

export default {
    name: "m-header",
    data() {
        return {
            logo
        };
    },
    computed: {
        ...mapState({ isLoggedIn: (state) => !!state.auth })
    },
    methods: {
        ...mapActions(["openLoginModal"]),
        logoutUser() {
            postData("/api/logout", {}, (res) => {
                // console.log(res.message);
                window.location.reload();
            });
        }
    }
};
</script>

<style lang="scss" scoped></style>
