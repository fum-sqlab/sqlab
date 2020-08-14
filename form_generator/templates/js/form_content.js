function localFormContent(_id){
  var form_id_val = _id;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myObj = JSON.parse(this.responseText);
      form = createForm(myObj);
      document.getElementById("edit_form_demo").innerHTML = form;
    }
  };
  var url = "http://127.0.0.1:8000/form/" + form_id_val + "/";
  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}

function createForm(_myObj) {
  text = '<form name="' + _myObj.title + '"><div class="container">';
  text += '<h2>' + _myObj.title + '</h2>';
  text += '<p>' + _myObj.description + '</p> <hr>';
    myObj = sort(_myObj.fields)
    for(i = 0; i< myObj.length; i++){
      if(myObj[i].field_type == "checkbox"){
        text += checkbox_field(myObj[i])
      }
      else{
        text += "<label for=\"" + myObj[i].id + "\">" + myObj[i].label + "</label><br>";
        text += "<input type=\"" + myObj[i].field_type + "\"" +
                "id=\"" + myObj[i].id + "\"" +
                "name=\"" + myObj[i].name + "\"" +
                "value=\""+ myObj[i].default_value + "\">" + "<br>";
      }
    } 
  text += "<div></form>";
  return text;
}

function checkbox_field(data){
  check = '<input type="checkbox" id="' + data.id + 
          '" name="' + data.name + 
          '" value="' + data.default_value + '">';
  check += '<label for="' + data.id + '">' +
            data.label +
            '</label><br>';
  
  return check;
}

function sort(data_list){
  for(i=0; i<data_list.length; i++){
    for(j=i+1; j<data_list.length; j++){
      if(data_list[i].placeHolder > data_list[j].placeHolder){
        k = data_list[i];
        data_list[i] = data_list[j];
        data_list[j] = k;
      }
    }
  }
  return data_list;
}