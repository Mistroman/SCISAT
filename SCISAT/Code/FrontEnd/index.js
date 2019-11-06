/**
* Author: Alireza Azimi, Manu Parashar
* Initialize 3D earth
*
*/

var options = {atmosphere: true, center: [0, 0], zoom: 1.5, zooming: false, atmosphere: true, sky: true};
var earth = new WE.map('map', options);
function initialize() {


  WE.tileLayer('http://tileserver.maptiler.com/nasa/{z}/{x}/{y}.jpg', {
          minZoom: 0,
          maxZoom: 5,
          attribution: 'NASA'
        }).addTo(earth);

}
