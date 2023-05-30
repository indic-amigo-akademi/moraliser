<style lang="scss" scoped></style>

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
              <router-link class="nav-link" active-class="active" to="/">
                Home
              </router-link>
            </li>
            <li class="nav-item" v-if="isGuest">
              <a class="nav-link" href="#" @click.prevent="openLoginModal">
                Login/Register
              </a>
            </li>
            <li class="nav-item" v-else>
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
              >
                {{ auth?.username }}
              </a>
              <ul class="dropdown-menu">
                <li>
                  <a href="#settings" class="dropdown-item"> Settings </a>
                </li>
                <li>
                  <a
                    href="#logout"
                    class="dropdown-item"
                    @click.prevent="logoutUser"
                  >
                    Logout
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script lang="ts">
import logo from "@/assets/logo.png";
import { mapActions, mapGetters, mapState } from "vuex";
import { logoutUser } from "@/utils/authUtils";

export default {
  name: "m-header",
  setup() {
    return {
      logo,
    };
  },
  mounted() {},
  computed: {
    ...mapGetters(["isGuest"]),
    ...mapState(["auth"]),
  },
  methods: {
    ...mapActions(["openLoginModal"]),
    logoutUser,
  },
};
</script>
