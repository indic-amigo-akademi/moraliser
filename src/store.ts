import { defineStore } from "pinia";
import type { UserInfo } from "./types/Models";

export const useAppStore = defineStore("app", {
  state: () => {
    return { isLoginModalOpen: false, auth: null as UserInfo | null };
  },
  actions: {
    closeLoginModal() {
      this.isLoginModalOpen = false;
    },
    openLoginModal() {
      this.isLoginModalOpen = true;
    },
    setAuthUser(user: UserInfo | null) {
      this.auth = user;
    },
  },
});
