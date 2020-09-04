function loadFormContent(_id){
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myObj = JSON.parse(this.responseText);
      form = createForm(myObj);
      document.getElementById("edit_form_demo").innerHTML = form;
    }
  };
  var url = "http://127.0.0.1:8000/form/" + _id + "/";
  xmlhttp.open("GET", url, true);
  xmlhttp.send();
}
function createForm(_myObj) {
  text = '<form name="' + _myObj.title + '"><div class="container">';
  text += '<h2>' + _myObj.title + '</h2>';
  text += '<p>' + _myObj.description + '</p> <hr>';
  myObj = sort(_myObj.fields)
  for(i = 0; i< myObj.length; i++){
    type = myObj[i].field_type;
    switch(type){
      case "checkbox":
        text += checkbox_field(myObj[i]);
        break;
      
      case "radio":
        text += radio_field(myObj[i]);
        break;

      case "boolean":
        text += boolean_field(myObj[i]);
        break;
      
      default:
        text += similar_field(myObj[i]);
        break;
    }
  } 
  text += "</div></form>";
  return text;
}
function checkbox_field(data){
  var items = data.items;
  var default_val = data.default_value;
  check = '<fieldset>';
  check += '<legend>' + data.label + '</legend>';
  for(i=0; i<items.length; i++){
    if(default_val == items[i].name){
      check += '<input type="checkbox" id="' + data.id + 
             '" name="' + data.name + 
             '" value="' + items[i].name + '" checked>' + 
             items[i].name + '<br>';
    }
    else{
      check += '<input type="checkbox" id="' + data.id + 
             '" name="' + data.name + 
             '" value="' + items[i].name + '">' + 
             items[i].name + '<br>';
    } 
  }
  return check;
}
function radio_field(data){
  var items = data.items;
  var default_val = data.default_value;
  check = '<fieldset>';
  check += '<legend>' + data.label + '</legend>';
  for(i=0; i<items.length; i++){
    if(default_val == items[i].name){
      check += '<input type="radio" id="' + data.id + 
               '" name="' + data.name + 
               '" value="' + items[i].name + '" checked>' + 
               items[i].name + '<br>';
    }
    else{
      check += '<input type="radio" id="' + data.id + 
             '" name="' + data.name + 
             '" value="' + items[i].name + '">' + 
             items[i].name + '<br>';
    } 
  }
  return check;
}
function similar_field(data){
  var type = data.field_type;
  if (type == "datetime"){
    type = "datetime-local";
  }
  label = "<label for=\"" + data.id + '"';
  text = "<input type=\"" + type + "\"" +
         "id=\"" + data.id + "\"" +
         "name=\"" + data.name + "\"" +
         "value=\""+ data.default_value + "\"";
  if( data.visible == false ){
    label += 'style="display: none;"';
    text += 'style="display: none;"';
  }
  if( data.enable == false ){
    label += "disabled";
    text += "disabled";
  }
  label += '>' + data.label + "</label><br>"
  text += '><br>';

  return label+text;
}
function boolean_field(data){
  if(data.default_value == true){
    return '<input type="checkbox" id="' + data.id + 
           '" name="' + data.name + 
           '" value="' + data.label + '" checked>' + 
           data.label + '<br>';
  }
  return '<input type="checkbox" id="' + data.id + 
           '" name="' + data.name + 
           '" value="' + data.label + '">' + 
           data.label + '<br>';
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