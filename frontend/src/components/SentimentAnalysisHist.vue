<template>
  <v-card class="mt-3">
    <v-card-title primary-title>
      <h3 class="headline mb-0">Sentiment Analysis Histogram</h3>
    </v-card-title>
    <v-card-text>
      <div id="sentiment">
      </div>
    </v-card-text>
  </v-card>
</template>
<script>
import { mapState } from "vuex";
import axios from "axios";
import Plotly from "plotly.js/dist/plotly.min.js";
export default {
  props: ["query"],
  methods: {
    async fetchData() {
      var qs = require("qs");
      const { data } = await axios.post(
        "http://localhost:8002/search/",
        qs.stringify({
          query: this.search
        })
      );
      var tweets = data.tweets;
      var plotData = [];
      for (let i = 0, len = tweets.length; i < len; i++) {
        plotData.push(tweets[i].polarity);
      }
      var trace = {
        x: plotData,
        type: "histogram"
      };
      var plot = [trace];
      Plotly.newPlot("sentiment", plot);
    }
  },
  beforeMount() {
    this.fetchData();
  }
};
</script>

