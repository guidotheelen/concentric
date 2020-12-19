import planetChartData from '../chartdata.js';

export const FatpercentageStats = new Vue({
  el: '#vue-fatpercentage-stats',
  delimiters: ['${', '}'],
  data: {
    datacollection: null,
    planetChartData: planetChartData
  },
  methods: {
    createChart(chartId, chartData) {
      const ctx = document.getElementById(chartId);
      console.log(ctx)
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options,
      });
    },

    getRandomInt: function () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }

  },
  mounted() {
    console.log("OI")
    this.createChart('planet-chart', this.planetChartData);
  }
})