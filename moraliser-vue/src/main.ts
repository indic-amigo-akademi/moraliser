import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { Icon } from "@iconify/vue";

// import "./filters";

import "bootstrap";
import "./styles/style.scss";

// Vue.config.productionTip = false;

const app = createApp(App);
app.use(router).use(store).component("m-icon", Icon).mount("#app");
