import { createStore } from "vuex";
import type { UserInfo } from "./types/Models";

interface AppStoreState {
  isLoginModalOpen: boolean;
  auth: null | UserInfo;
}
interface AppStoreAction {
  isOpen: boolean;
  user: null | UserInfo;
}

export default createStore({
  state: () => {
    return {
      isLoginModalOpen: false as boolean,
      auth: null as UserInfo | null,
    };
  },
  mutations: {
    toggleLoginModal(state: AppStoreState, { isOpen }: AppStoreAction) {
      state.isLoginModalOpen = isOpen;
    },
    setAuthUser(state: AppStoreState, { user }: AppStoreAction) {
      state.auth = user;
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
    isGuest(state): boolean {
      return state.auth == null;
    },
  },
});
