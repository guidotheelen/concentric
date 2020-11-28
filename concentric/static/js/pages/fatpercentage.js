export const FatpercentageMeasurements = new Vue({
    el: '#vue-fatpercentage-measurements',
    delimiters: ['${', '}'],
    data: {
      Pollock3: false,
      Pollock4: false,
      Pollock7: false,
      Womersley: false,
      Digital: false
    },
    methods: {
      turnOffAllMeasurements: function () {
        this.Pollock3 = false;
        this.Pollock4 = false;
        this.Pollock7 = false;
        this.Womersley = false;
        this.Digital = false;
      },
      choose_measurement: function (measurement) {
        this.turnOffAllMeasurements();
        switch(measurement) {
          case "Pollock3":
            this.Pollock3 = true;
            break;
          case "Pollock4":
            this.Pollock4 = true;
            break;
          case "Pollock7":
            this.Pollock7 = true;
            break;
          case "Womersley":
            this.Womersley = true;
            break;
          case "Digital":
            this.Digital = true;
            break;
        }
      }
    }
  })