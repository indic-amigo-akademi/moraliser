<template>
    <div class="home">
        <MHelloWorld msg="Welcome to Moraliser" />

        <div
            class="modal fade reglogModal"
            id="reglogModal"
            tabindex="-1"
            role="dialog"
            aria-labelledby="reglogModalTitleId"
            aria-hidden="true"
        >
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>

                    <div class="modal-header">
                        <ul class="nav nav-pills mx-auto" id="reglogFormTab" role="tablist">
                            <li class="nav-item" role="presentation">
                                <a
                                    class="nav-link active"
                                    id="register-tab"
                                    data-toggle="tab"
                                    href="#register"
                                    role="tab"
                                    aria-controls="register"
                                    aria-selected="true"
                                >
                                    Register
                                </a>
                            </li>
                            <li class="nav-item" role="presentation">
                                <a
                                    class="nav-link"
                                    id="login-tab"
                                    data-toggle="tab"
                                    href="#login"
                                    role="tab"
                                    aria-controls="login"
                                    aria-selected="false"
                                >
                                    Login
                                </a>
                            </li>
                        </ul>
                    </div>

                    <div class="modal-body">
                        <div class="tab-content" id="reglogFormTabContent">
                            <div
                                class="tab-pane fade show active"
                                id="register"
                                role="tabpanel"
                                aria-labelledby="register-tab"
                            >
                                <MRegisterForm />
                            </div>
                            <div class="tab-pane fade" id="login" role="tabpanel" aria-labelledby="login-tab">
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

export default {
    name: "m-home",
    components: {
        MHelloWorld,
        MLoginForm,
        MRegisterForm
    }
};
</script>

<style lang="scss">
.reglogModal {
    .modal-content {
        position: relative;
        .close {
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
