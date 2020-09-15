function shoow(){
    var selectID = document.getElementById("select").selectedIndex;
    var formID = document.getElementsByTagName("option")[selectID].id;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var objForm = JSON.parse(this.responseText);
        document.getElementById("forms").innerHTML = create_table(objForm, formID);
      }
    };
    var url = "http://127.0.0.1:8000/answer/" + formID + "/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function create_table(data, id) {
  sub_data = data["submission"];
  field_names = data["fields"];
  sub_len = data["submission"].length;
  field_len = data["fields"].length;

  var table= '<table class="table table-striped">';
  var head = '<thead><tr>';
  var body = '<tbody>';
  /* Table Header */
  for(var i = 0; i<field_len; i++){
    head += '<th scope="col">' + field_names[i] + '</th>';
  }
  head += '</tr></head>';

  /* Table Body */
  for(var j = 0; j<sub_len; j++){
    body += '<tr>';
    answer = sub_data[j]["fields"];
    for(var k = 0; k<field_len; k++){
      flag = 0;
      for(var ind = 0; ind < answer.length; ind++){
        if (field_names[k] == answer[ind]["name"]){
          body += '<td>' + answer[ind]["value"] + '</td>';
          flag = 1;
        }
      }
      if(flag == 0){
        body += '<td></td>';
      }
    }
    body += '</tr>';
  }

  body += '<tr><td colspan="'+ field_len +'"><button id="' + id + '" type ="button" class ="btn btn-success" onclick="set(this.id)">+</button></td></tr>';
  
  body += '</tbody>';
  table += (head+body+'</table>');
  return table;
}
