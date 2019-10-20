function drawGraph(dataSets, labels, dataSetLabels){

let myChart = document.getElementById("myChart").getContext('2d');
      let gasConcChart = new Chart(myChart, {
        type:'line',
        data:{
          labels: labels,
          datasets:[{

              data: dataSets[0],
              label: dataSetLabels[0],
              borderColor: "#3e95cd",
              fill: false

          }]
        },
        options:{
          title: {
          display: true,
          text: 'Gas Concentration of Ozone vs Time'
        },

        scales: {
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Gas Concentration (ppm)'
            }
              
          }],

          xAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'Time'
            }
              
          }]
      }
      }
      });

    }