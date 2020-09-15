function get_all_forms() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          var all_forms = JSON.parse(this.responseText);
          show_all_forms(all_forms);        
      }
    };
    xhttp.open("GET", "http://127.0.0.1:8000/form/", true);
    xhttp.send(null);
}
function show_all_forms(data){
    var text = '<div class="p-5">'+
               '<select id="select" multiple  class="commits2 form-control" size=20>';
    for(var i = 0; i<data.length; i++){
        text += '<option id="' + data[i].id + '">' +
                data[i].title +
                '</option>';
    }//set in Show button
    text += '</select></div>';
    text += '<div class="text-right"><div class = "btn-group">' +
            '<div class="btn-group">' +
            '<button type ="button" class ="btn btn-success" onclick="show()">Show</button>'+ 
            '</div><div class="btn-group">' +
            '<button type = "button" class = "btn btn-danger" onclick="cancel()">Cancel</button>'+
            '</div></div></div>';
    
    document.getElementById("forms").innerHTML = text;
}
