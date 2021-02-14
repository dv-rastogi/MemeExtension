// import {findMeme} from "../src/index.js";
function myNewFunction() {
    var text=window.getSelection().toString();
    //alert(text);
    return text;
  }

function httpGet(theUrl)
  {
      if (window.XMLHttpRequest)
      {// code for IE7+, Firefox, Chrome, Opera, Safari
          xmlhttp=new XMLHttpRequest();
      }
      else
      {// code for IE6, IE5
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
      }
      xmlhttp.onreadystatechange=function()
      {
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
          {
                var modal = document.getElementById("myModal");
                var img = document.getElementById("myImg");
                var modalImg = document.getElementById("img01");
                var captionText = document.getElementById("caption"); 
                alert(xmlhttp.responseText);
                console.log(xmlhttp.responseText);
                return xmlhttp.responseText;
          }
      }
      xmlhttp.open("GET", theUrl, false );
      xmlhttp.send();    
  }
  function httpGetSound(theUrl)
  {
      if (window.XMLHttpRequest)
      {// code for IE7+, Firefox, Chrome, Opera, Safari
          xmlhttp=new XMLHttpRequest();
      }
      else
      {// code for IE6, IE5
          xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
      }
      xmlhttp.onreadystatechange=function()
      {
          if (xmlhttp.readyState==4 && xmlhttp.status==200)
          {
            var audio =new Audio("sound.wav");
            audio.play();
          }
      }
      xmlhttp.open("GET", theUrl, false );
      xmlhttp.send();    
  }
var t=myNewFunction();
httpGet('http://127.0.0.1:5000/getUrban/definition/'+t)
httpGetSound('http://127.0.0.1:5000/getUrban/sound/'+t);