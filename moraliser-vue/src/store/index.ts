import { createStore } from "vuex";
import type { UserInfo } from "../types/Models";

export interface AppStoreState {
  isLoginModalOpen: boolean;
  auth: UserInfo | null;
  csrf_token: string | null;
}
export interface AppStoreAction {
  isOpen: boolean;
  user: UserInfo | null;
  csrf_token: string | null;
}

export default createStore({
  state: () => {
    return {
      isLoginModalOpen: false,
      auth: null,
      csrf_token: null,
    };
  },
  mutations: {
    toggleLoginModal(state: AppStoreState, { isOpen }: AppStoreAction) {
      state.isLoginModalOpen = isOpen;
    },
    setAuthUser(state: AppStoreState, { user, csrf_token }: AppStoreAction) {
      state.auth = user;
      state.csrf_token = csrf_token;
    },
  },
  actions: {
    closeLoginModal({ commit }) {
      commit("toggleLoginModal", { isOpen: false });
    },
    openLoginModal({ commit }) {
      commit("toggleLoginModal", { isOpen: true });
    },
  },
  getters: {
    isGuest: (state: AppStoreState) => {
      return !state.auth;
    },
  },
});
