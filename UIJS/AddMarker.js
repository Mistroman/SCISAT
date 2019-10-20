function NewMarker(lat, long, markerMess){
    var marker = WE.marker([lat, long]).addTo(earth);
        
        marker.bindPopup("<b><span id='myText'></span></b>", {maxWidth: 150, closeButton: true}).openPopup();
        document.getElementById("myText").innerHTML = markerMess;

}