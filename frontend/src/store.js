import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    tweets: []
  },
  mutations: {
    SET_TWEETS(state, data) {
      state.tweets = [];
      for (let i = 0, len = data.length; i < len; i++) {
        state.tweets.push(data[i]);
      }
    }
  },
  actions: {}
});
