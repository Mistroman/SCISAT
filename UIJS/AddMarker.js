function NewMarker(lat, long, markerMess){
    var marker = WE.marker([lat, long]).addTo(earth)
    marker.bindPopup('<b>Hello world!</b>');

}