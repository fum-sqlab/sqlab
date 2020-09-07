function get_all_forms(section_id) {
    var _id = section_id.id;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          var all_forms = JSON.parse(this.responseText);
          show_all_forms(_id, all_forms);        
      }
    };
    xhttp.open("GET", "http://127.0.0.1:8000/form/", true);
    xhttp.send(null);
}
function show_all_forms(_id, data){
    var text = '<div class="p-5">'+
               '<select id="select'+ _id +'" multiple  class="commits2 form-control" size=20>';
    for(var i = 0; i<data.length; i++){
        text += '<option id="' + data[i].id + '">' +
                data[i].title +
                '</option>';
    }
    text += '</select></div>';
    text += '<div class="text-right"><div class = "btn-group">' +
            '<div class="btn-group">' +
            '<button id="s_'+ _id +'" type ="button" class ="btn btn-success" onclick="set(this.id)">Set</button>'+
            '</div><div class="btn-group">' +
            '<button id="c_'+ _id +'" type = "button" class = "btn btn-danger" onclick="cancel(this.id)">Cancel</button>'+
            '</div></div></div>';
    
    document.getElementById("form"+_id).innerHTML = text;
}
