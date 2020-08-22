function DeleteForm(){
    var form_id_val =  document.getElementById("form_id").value;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var myObj = JSON.parse(this.responseText);
        document.getElementById("form_demo").innerHTML = JSON.stringify(myObj);
      }
    };
    var url = "http://127.0.0.1:8000/form/" + form_id_val + "/";
    xmlhttp.open("DELETE", url, true);
    xmlhttp.send(null);
    
    xmlhttp.onload = function () {
      if (xmlhttp.status == 204){
        window.location.reload();
      }
    };
    
}