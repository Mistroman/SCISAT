console.log("Hi in Main");
      $.getJSON("sample.json", function(json) {
       let alt_conc = json.alt_conc[0];
       for(i = 0; i< alt_conc.length; i++){
           if(alt_conc[i][1] > 10 || alt_conc[i][1] < 0){
            alt_conc.splice(i, 1);
            i--;
           }
       }
       drawGraph(alt_conc, "Ozone");
       let altitudes = [];
       let ozoneConc = [];

       for(i = 0; i < alt_conc.length; i++){
           altitudes[i] = alt_conc[i][2];
           ozoneConc[i] = alt_conc[i][1];

       }
       drawConcentratonLayers(altitudes, ozoneConc);

      });