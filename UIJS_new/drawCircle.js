function drawCircle(x,y,r,sangle,eangle,color){
    console.log("inside drawCircle");
    //ctx.fillStyle = "#c82124";
    let c = document.getElementById("concLayers");
    let ctx = c.getContext("2d");
    ctx.beginPath();
    ctx.arc(x, y, r, sangle, eangle);
    ctx.strokeStyle = color;
    ctx.stroke();
    
}