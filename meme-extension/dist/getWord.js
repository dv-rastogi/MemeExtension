// import {findMeme} from "../src/index.js";
var modal = document.getElementById("myModal");
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption"); 
var def;
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

                alert("UD says:\n"+xmlhttp.responseText);
                return xmlhttp.responseText;
          }
      }
      xmlhttp.open("GET", theUrl, false );
      xmlhttp.send();   
  }
  function httpGetImage(theUrl)
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
                // modalImg.src = xmlhttp.responseText;
                // captionText.innerHTML = this.alt;
                // var span = document.getElementsByClassName("close")[0];
                // span.onclick = function() {
                //     modal.style.display = "none";
                // }
                var x = document.getElementsByTagName("body")[0];
                var imageModal=`<style>#myImg {
                    border-radius: 5px;
                    cursor: pointer;
                    transition: 0.3s;
                  }
                  
                  #myImg:hover {opacity: 0.7;}
                  
                  /* The Modal (background) */
                  .modal {
                    position: absolute; /* Stay in place */
                    z-index: 1000; /* Sit on top */
                    padding-top: 100px; /* Location of the box */
                    left: 100;
                    top: 100;
                    width: 100%; /* Full width */
                    height: 100%; /* Full height */
                    overflow: auto; /* Enable scroll if needed */
                    background-color: rgb(0,0,0); /* Fallback color */
                    background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
                  }
                  
                  /* Modal Content (Image) */
                  .modal-content {
                    margin: auto;
                    display: block;
                    width: 80%;
                    max-width: 700px;
                  }
                  
                  /* Caption of Modal Image (Image Text) - Same Width as the Image */
                  #caption {
                    margin: auto;
                    display: block;
                    width: 80%;
                    max-width: 700px;
                    text-align: center;
                    color: #ccc;
                    padding: 10px 0;
                    height: 150px;
                  }
                  
                  
                  /* 100% Image Width on Smaller Screens */
                  @media only screen and (max-width: 700px){
                    .modal-content {
                      width: 100%;
                    }
                  }</style>
                <div id="myModal" class="modal">
                <img class="modal-content" src="${xmlhttp.responseText}" id="img01">
                <div id="caption"></div>
                </div>`
                x.innerHTML+=imageModal;
                console.log(xmlhttp.responseText);
                return xmlhttp.responseText;
          }
      }
      xmlhttp.open("GET", theUrl, true );
      xmlhttp.send();   
  }
var t=myNewFunction();
try {    
  httpGet('http://127.0.0.1:5000/getUrban/definition/'+t)
  httpGetImage('http://127.0.0.1:5000/getSpecificMeme/'+t)
} catch (err) {
  console.log("Error");
}
src="${xmlhttp.responseText}"
//httpGetSound('http://127.0.0.1:5000/getUrban/sound/'+t);