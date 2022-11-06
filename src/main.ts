import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

// import "./filters";

import "bootstrap";
import "./styles/style.scss";

// Vue.config.productionTip = false;

const app = createApp(App).use(store).use(router);
app.mount("#app");
