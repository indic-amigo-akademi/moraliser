import { createStore } from "vuex";

export default createStore({
    state() {
        return {
            isLoginModalOpen: false,
            auth: null
        };
    },
    mutations: {
        toggleLoginModal(state, { isOpen }) {
            state.isLoginModalOpen = isOpen;
        },
        setAuthUser(state, { user }) {
            state.auth = user;
        }
    },
    actions: {
        closeLoginModal({ commit }) {
            commit("toggleLoginModal", { isOpen: false });
        },
        openLoginModal({ commit }) {
            commit("toggleLoginModal", { isOpen: true });
        }
    }
});
