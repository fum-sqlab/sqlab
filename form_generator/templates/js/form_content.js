function localFormContent(){
    var form_id_val =  document.getElementById("form_id").value;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var myObj = JSON.parse(this.responseText);
        form = createForm(myObj);
        document.getElementById("form_demo").innerHTML = form;
      }
    };
    var url = "http://127.0.0.1:8000/form/" + form_id_val + "/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function createForm(myObj) {
    text = "<form>"
      for(i = 0; i< myObj.fields.length; i++){
        text += "<label for=\"" + myObj.fields[i].id + "\">" + myObj.fields[i].label + "</label><br>";
        text += "<input type=\"" + myObj.fields[i].field_type + "\"" +
                "id=\"" + myObj.fields[i].id + "\"" +
                "name=\"" + myObj.fields[i].name + "\"" +
                "value=\""+ myObj.fields[i].default_value + "\">" + "<br>";
      } 
      text += "</form>";
      return text;
}