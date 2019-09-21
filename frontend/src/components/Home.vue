<template>
  <div class="home">
    <v-text-field
      v-model="search"
      append-icon="search"
      label="Search"
      single-line
      v-on:keyup.13="submit"
    ></v-text-field>
    <v-flex xs-12>
      <v-card class="mt-2" v-if="tweets.length != 0">
        <v-card-title primary-title>
          <h3 class="headline mb-0">Tweets</h3>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="tweets"
          :loading="loading"
          class="align-center"
        >
        <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
          <template slot="items" slot-scope="tweet">
            <td>{{ tweet.item.user }}</td>
            <td>{{ tweet.item.text }}</td>
            <td>{{ tweet.item.created_at }}</td>
            <td>{{ tweet.item.polarity }}</td>
          </template>
        </v-data-table>
      </v-card>
      <div v-if="tweets.length != 0">
        <SentimentAnalysisHist :query="search"></SentimentAnalysisHist>
      </div>
    </v-flex>
  </div>
</template>
<script>
import axios from "axios";
import { mapState } from "vuex";
import store from "@/store";
import SentimentAnalysisHist from "@/components/SentimentAnalysisHist.vue";
export default {
  components: {
    SentimentAnalysisHist
  },
  data() {
    return {
      search: "",
      loading: true,
      pagination: {
        descending: true,
        sortBy: "created_at",
        rowsPerPage: 10
      },
      headers: [
        {
          text: "User",
          align: "left",
          value: "user",
          sortable: false
        },
        {
          text: "Text",
          value: "text",
          sortable: false
        },
        {
          text: "Tweeted At",
          value: "created_at",
          sortable: true
        },
        {
          text: "Polarity",
          value: "polarity",
          sortable: true
        }
      ]
    };
  },
  methods: {
    submit() {
      this.fetchSearchResults();
    },

    async fetchSearchResults() {
      console.log({
        query: this.search
      });
      var qs = require("qs");
      const { data } = await axios.post(
        "http://localhost:8002/search/",
        qs.stringify({
          query: this.search
        })
      );
      this.loading = false;
      store.commit("SET_TWEETS", data.tweets);
    }
  },
  computed: {
    ...mapState(["tweets"])
  }
};
</script>

