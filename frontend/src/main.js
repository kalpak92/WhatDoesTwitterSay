import "@babel/polyfill";
import Vue from "vue";
import axios from "axios";

import "./plugins/vuetify";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

axios.defaults.headers.common["Accept"] = "application/json";

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
