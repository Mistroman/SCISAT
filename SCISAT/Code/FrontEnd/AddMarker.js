/**
* Author: Alireza Azimi, Manu Parashar
* Adds marker to earth
*
*/

function NewMarker(lat, long, markerMess = ""){
    var marker = WE.marker([lat, long]).addTo(earth);
    var message = "<b><span id='myText'>" + "Latitude: "+lat+"<br/>" + "Longitude: " + long + "</span></b>";

        marker.bindPopup(message, {maxWidth: 150, closeButton: true});

        document.getElementById("myText").innerHTML = markerMess;

}
