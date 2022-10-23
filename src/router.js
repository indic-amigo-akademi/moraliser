import { createRouter, createWebHashHistory } from "vue-router";
import Home from "./views/Home.vue";
import Chat from "./views/Chat.vue";

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: "/",
            name: "home",
            component: Home
        },
        {
            path: "/demo-chat",
            name: "chat",
            component: Chat
        }
    ]
});
