import { createStore } from "vuex";

interface AppStoreState {
    isLoginModalOpen: boolean;
    auth: null | User;
}
interface AppStoreAction {
    isOpen: boolean;
    user: null | User;
}

export default createStore({
    state() {
        return {
            isLoginModalOpen: false,
            auth: null
        };
    },
    mutations: {
        toggleLoginModal(state: AppStoreState, { isOpen }: AppStoreAction) {
            state.isLoginModalOpen = isOpen;
        },
        setAuthUser(state: AppStoreState, { user }: AppStoreAction) {
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
