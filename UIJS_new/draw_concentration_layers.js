function drawConcentratonLayers(altitudes, ozoneConcentrations){
    // center should always be x: 102, y: 182

    console.log(altitudes);
    console.log(ozoneConcentrations);
    
    var mapRange = function(from, to, s) {
      return to[0] + (s - from[0]) * (to[1] - to[0]) / (from[1] - from[0]);
    }
    
    let min_conc = Math.min.apply(null, ozoneConcentrations);
    let max_conc = Math.max.apply(null, ozoneConcentrations);
    for(i = 0; i<altitudes.length; i++){
        let color_string;
       
        var r = mapRange([max_conc,min_conc], [0,255], ozoneConcentrations[i]);
        var radius = mapRange([5, 160], [102, 182], altitudes[i]);
        rs = r.toString(10);
        //console.log(r);
        color_string  = "rgb(255," + rs +", "+ rs +")";
        //console.log(color_string);
        drawCircle(102, 182, radius, 0, 2*Math.PI, color_string);
      }

      
      

  }