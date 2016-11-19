//	Document pour l'execution de fonctionalites dynamiques
// 	Fonction de traitement pour les buttons de l'image
//	Fonction de traitement du menu


// Requete AJAX pour linteration dans le serveur.
var zoom = 1;
function traitement()
{
// Variables de transmition pour le serveur
    var real = document.getElementById("real").value,
    image =  document.getElementById("imagejulia"),
    imag = document.getElementById("imag").value,
    n_int = document.getElementById("interatition").value,
    color_num = document.getElementById("color_number").value,
    down = document.getElementById("downloadimage"),
    r = new XMLHttpRequest();

    zoom = 1;
// Image de chargement
    image.width = 40;
    image.src = "style/processing.gif";

//Requete asynchrone
    r.onload = function() {
        image.width = 400;
        image.src = "images/"+real.split(".")[0]+real.split(".")[1]+"_"+imag.split(".")[0]+imag.split(".")[1]+"_"+n_int.toString()+"_"+color_num+"_"+zoom+".png";
	down.href = "images/"+real.split(".")[0]+real.split(".")[1]+"_"+imag.split(".")[0]+imag.split(".")[1]+"_"+n_int.toString()+"_"+color_num+"_"+zoom+".png";
	down.download = "images/"+real.split(".")[0]+real.split(".")[1]+"_"+imag.split(".")[0]+imag.split(".")[1]+"_"+n_int.toString()+"_"+color_num+"_"+zoom+".png";
    };
// Envoie de requete du type GET.
        r.open("GET","/service/"+real+"/"+imag+"/"+n_int.toString()+"/"+color_num+"/1",true);
        r.send()
}

function traitement_zoom_pos()
{
    var real = document.getElementById("real").value,
    image =  document.getElementById("imagejulia"),
    imag = document.getElementById("imag").value,
    n_int = document.getElementById("interatition").value,
    color_num = document.getElementById("color_number").value,
    down = document.getElementById("downloadimage"),
    r = new XMLHttpRequest();
    if(zoom + 1 <= 10)
    {
        zoom = zoom+1;
    }
    
    image.width = 40;
    image.src = "style/processing.gif";
    
    r.onload = function() {
        image.width = 400;
        image.src = "images/"+real.split(".")[0]+real.split(".")[1]+"_"+imag.split(".")[0]+imag.split(".")[1]+"_"+n_int.toString()+"_"+color_num+"_"+zoom+".png";
        //  down.href = image.src;
	        down.href = "images/"+real.split(".")[0]+real.split(".")[1]+"_"+imag.split(".")[0]+imag.split(".")[1]+"_"+n_int.toString()+"_"+color_num+"_"+zoom+".png";
        down.download = "images/"+real.split(".")[0]+real.split(".")[1]+"_"+imag.split(".")[0]+imag.split(".")[1]+"_"+n_int.toString()+"_"+color_num+"_"+zoom+".png";
    };
    
    r.open("GET","/service/"+real+"/"+imag+"/"+n_int.toString()+"/"+color_num+"/"+zoom,true);
    r.send()
}


function traitement_zoom_neg()
{
    var real = document.getElementById("real").value,
    image =  document.getElementById("imagejulia"),
    imag = document.getElementById("imag").value,
    n_int = document.getElementById("interatition").value,
    color_num = document.getElementById("color_number").value,
    down = document.getElementById("downloadimage"),
    r = new XMLHttpRequest();
    if(zoom - 1 >= 1)
    {
        zoom = zoom-1;
    }
    image.width = 40;
    image.src = "style/processing.gif";
    
    r.onload = function() {
        image.width = 400;
        image.src = "images/"+real.split(".")[0]+real.split(".")[1]+"_"+imag.split(".")[0]+imag.split(".")[1]+"_"+n_int.toString()+"_"+color_num+"_"+zoom+".png";
        //  down.href = image.src;
        down.href = "images/"+real.split(".")[0]+real.split(".")[1]+"_"+imag.split(".")[0]+imag.split(".")[1]+"_"+n_int.toString()+"_"+color_num+"_"+zoom+".png";
        down.download = "images/"+real.split(".")[0]+real.split(".")[1]+"_"+imag.split(".")[0]+imag.split(".")[1]+"_"+n_int.toString()+"_"+color_num+"_"+zoom+".png";

    };
    
    r.open("GET","/service/"+real+"/"+imag+"/"+n_int.toString()+"/"+color_num+"/"+zoom,true);
    r.send()
}



// Fonctionalites dynamiques du menu
function openNav()
{
        document.getElementById("mySidenav").style.width = "250px";
}

function closeNav()
{
        document.getElementById("mySidenav").style.width = "0";
}
