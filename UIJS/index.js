var options = {atmosphere: true, center: [0, 0], zoom: 1.5, zooming: false, atmosphere: true, sky: true};
var earth = new WE.map('map', options);
function initialize() {
  
  
  WE.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
          minZoom: 0,
          maxZoom: 5,
          attribution: 'NASA'
        }).addTo(earth);
        
      }
    
