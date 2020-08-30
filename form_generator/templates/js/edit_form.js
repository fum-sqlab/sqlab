function loadFormContent(_id){
    var form_id_val = _id;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var myObj = JSON.parse(this.responseText);
        form(myObj);
      }
    };
    var url = "http://127.0.0.1:8000/form/" + form_id_val + "/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function localFieldContent(callback){
    var xmlhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/field/";
    xmlhttp.open("GET", url, true);
    xmlhttp.onreadystatechange = function() {
        returned_data = xmlhttp.responseText;
    };
    xmlhttp.send("");
}

function form(data){
    document.getElementById("ID").innerHTML = '<label id="id">' + data.id + '</label>';
    document.getElementById("Title").innerHTML = '<input type="text" id="title" name="title" value="'
                                                 + data.title
                                                 + '">';
    document.getElementById("Description").innerHTML = '<textarea type="text" id="description" name="description"'
                                                       + '" style="height:200px">'+ data.description +'</textarea>';
    document.getElementById("checkboxes").innerHTML = checkbox_check_l(data.enable , "enable") +
                                                      checkbox_check_l(data.visible, "visible");

    for(i=0; i<data.fields.length; i++){
        field(data.fields, i);
    }
    
}

function checkbox_check_l(data, type){
    var TYPE;
    if (type == "enable"){
        TYPE = "Enable";
    }
    else{
        TYPE = "Visible"
    }
    
    if(data == true){
        return '<input id="' + type + '-f' + '" type="checkbox" checked="checked">' + 
               '<label for="' + type + '-f' + '">' + TYPE + '</label>';
    }
    else{
        return '<input id="' + type + '-f' + '" type="checkbox">' + 
               '<label for="' + type + '-f' + '">' + TYPE + '</label>';
    }
}

function field(fields, index){

    var table = document.getElementById("myTable");  
    var row = table.insertRow(1);
    var id = row.insertCell(0);
    var name = row.insertCell(1);
    var label = row.insertCell(2);
    var type = row.insertCell(3);
    var required = row.insertCell(4);
    var visible = row.insertCell(5);
    var enable = row.insertCell(6);
    var description = row.insertCell(7);
    var min_value = row.insertCell(8);
    var max_value = row.insertCell(9);
    var default_value = row.insertCell(10);
    var placeholder = row.insertCell(11);
    var deleted = row.insertCell(12);

    id.innerHTML = fields[index].id; 
    name.innerHTML = '<input id="name" type="text" value="' + fields[index].name + '">';
    label.innerHTML = '<input id="name" type="text" value="' + fields[index].label + '">';
    type.innerHTML = '<label>' + fields[index].field_type + '</label>';
    required.innerHTML = checkbox_check_nl(fields[index].required, "required", fields[index].id);
    visible.innerHTML = checkbox_check_nl(fields[index].visible, "visible", fields[index].id);
    enable.innerHTML = checkbox_check_nl(fields[index].enable, "enable", fields[index].id);
    description.innerHTML = '<input id="name" type="text" value="' + fields[index].description + '">';
    min_value.innerHTML = '<input id="name" type="text" value="' + fields[index].min_value + '">';
    max_value.innerHTML = '<input id="name" type="text" value="' + fields[index].max_value + '">';
    default_value.innerHTML = '<input id="name" type="text" value="' + fields[index].default_value + '">';
    placeholder.innerHTML = '<input id="name" type="text" value="' + fields[index].placeHolder + '">';
    deleted.innerHTML = '<button class="w3-button w3-red w3-padding-small" onclick="helper(this)">-</button>';

    id.style.display = "none";
}

function checkbox_check_nl(data, type, id){
    if(data == true){
        return '<input id="'+ type + '-' + id + '" type="checkbox" checked="checked">'
    }
    else{
        return '<input id="'+ type + '-' + id + '" type="checkbox">'
    }
}
