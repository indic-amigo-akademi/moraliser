import { createRouter, createWebHashHistory } from "vue-router";
import Home from "./views/MHome.vue";
import Chat from "./views/MChat.vue";

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/demo-chat",
      name: "chat",
      component: Chat,
    },
  ],
});
