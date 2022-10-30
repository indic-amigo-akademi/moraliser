<style lang="scss" scoped>
.reg-log-modal {
    display: block;
    background-color: rgba(#111, 0.25);
    .modal-content {
        position: relative;
        .btn-close {
            position: absolute;
            right: 1rem;
            top: 1rem;
        }
        .modal-body {
            height: 400px;
            .btn-container {
                position: absolute;
                left: 50%;
                bottom: 1rem;
                transform: translateX(-50%);
            }
        }
    }
}
</style>

<template>
    <div class="home">
        <MHelloWorld msg="Welcome to Moraliser" />

        <div
            class="modal fade show reg-log-modal"
            id="regLogModal"
            tabindex="-1"
            v-if="isLoginModalOpen"
            aria-model="true"
            role="dialog"
        >
            <div class="modal-dialog modal-dialog-scrollable" role="document">
                <div class="modal-content">
                    <button
                        type="button"
                        class="btn-close"
                        aria-label="Close"
                        @click.prevent="closeLoginModal"
                    ></button>

                    <div class="modal-header">
                        <ul class="nav nav-pills mx-auto" id="reglogFormTab" role="tablist">
                            <li class="nav-item" role="presentation">
                                <button
                                    id="register-tab"
                                    class="nav-link active"
                                    data-bs-toggle="tab"
                                    data-bs-target="#registerTabPane"
                                    role="tab"
                                    aria-controls="register"
                                    aria-selected="true"
                                >
                                    Register
                                </button>
                            </li>
                            <li class="nav-item" role="presentation">
                                <button
                                    id="login-tab"
                                    class="nav-link"
                                    role="tab"
                                    data-bs-toggle="tab"
                                    data-bs-target="#loginTabPane"
                                    aria-controls="loginTabPane"
                                    aria-selected="false"
                                >
                                    Login
                                </button>
                            </li>
                        </ul>
                    </div>

                    <div class="modal-body">
                        <div class="tab-content" id="reglogFormTabContent">
                            <div
                                class="tab-pane fade show active"
                                id="registerTabPane"
                                role="tabpanel"
                                aria-labelledby="register-tab"
                            >
                                <MRegisterForm />
                            </div>
                            <div class="tab-pane fade" id="loginTabPane" role="tabpanel" aria-labelledby="login-tab">
                                <MLoginForm />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import MHelloWorld from "@/components/MHelloWorld.vue";
import MLoginForm from "@/components/MLoginForm.vue";
import MRegisterForm from "@/components/MRegisterForm.vue";
import { mapActions, mapState } from "vuex";

export default {
    name: "m-home",
    components: {
        MHelloWorld,
        MLoginForm,
        MRegisterForm
    },
    computed: {
        ...mapState(["isLoginModalOpen"])
    },
    methods: {
        ...mapActions(["closeLoginModal"])
    }
};
</script>
