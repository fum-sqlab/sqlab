function localFormContent(_id){
    var form_id_val = _id;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var myObj = JSON.parse(this.responseText);
        form(myObj)
        // document.getElementById("edit_form_demo").innerHTML = _form;
      }
    };
    var url = "http://127.0.0.1:8000/form/" + form_id_val + "/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function form(data){
    document.getElementById("title").innerHTML = '<input type="text" id="text" name="title" value="'
                                                 + data.title
                                                 + '">';
    document.getElementById("description").innerHTML = '<textarea type="text" id="description" name="description"'
                                                       + '" style="height:200px">'+ data.description +'</textarea>';
    document.getElementById("checkboxes").innerHTML = checkbox_check(data.enable , "enable") + checkbox_check(data.visible, visible);
}
function checkbox_check(data, type){
    TYPE = {
        enable : "Enable",
        visible : "Visible"
    }
    type += "-f";
    if(data == true){
        return '<input id="' + type + '" type="checkbox" checked>' + 
               '<label for="' + type + '>' + TYPE.type  + '</label>';
    }
    else{
        return '<input id="' + type + '" type="checkbox">' + 
               '<label for="' + type + '>' + TYPE.type  + '</label>';
    }
}
