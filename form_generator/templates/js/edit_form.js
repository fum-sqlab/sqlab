function localFormContent(_id){
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
               '<label for="' + type + '-f' + '>' + TYPE + '</label>';
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
    var description = row.insertCell(6);
    var min_value = row.insertCell(7);
    var max_value = row.insertCell(8);
    var default_value = row.insertCell(9);
    var placeholder = row.insertCell(10);
    var deleted = row.insertCell(11);

    id.innerHTML = fields[index].id; 
    name.innerHTML = '<input id="name" type="text" value="' + fields[index].name + '">';
    label.innerHTML = '<input id="name" type="text" value="' + fields[index].label + '">';
    // - 
    required.innerHTML = checkbox_check_nl(fields[index].required, "required", fields[index].id);
    visible.innerHTML = checkbox_check_nl(fields[index].visible, "visible", fields[index].id);
    description.innerHTML = '<input id="name" type="text" value="' + fields[index].description + '">';
    min_value.innerHTML = '<input id="name" type="text" value="' + fields[index].min_value + '">';
    max_value.innerHTML = '<input id="name" type="text" value="' + fields[index].max_value + '">';
    default_value.innerHTML = '<input id="name" type="text" value="' + fields[index].default_value + '">';
    placeholder.innerHTML = '<input id="name" type="text" value="' + fields[index].placeholder + '">';
    deleted.innerHTML = '<button class="w3-button w3-red w3-padding-small" onclick="helper(this)">-</button>';

    id.style.display = "none";
}

function checkbox_check_nl(data, type, id){
    if(data == true){
        return '<input id="'+ type + '-' + id + '" type="checkbox" checked>'
    }
    else{
        return '<input id="'+ type + '-' + id + '" type="checkbox">'
    }
}

function delete_field(id){
    var table = document.getElementById("myTable");
    var field_id = table.rows[id].cells.item(0).innerHTML;
    var xmlhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/form/remove_field/" + field_id + "/";
    xmlhttp.open("DELETE", url, true);
    xmlhttp.send(null);
}


// function make_selector_field(data, selected){
//     select = '<select id="field" name="field">';
//     for(i=0; i<data.length; i++){
//         if(data[i].field_type == selected){
//             select += '<option ' + '" value="' + data[i].id +  '" selected>' +
//                 data[i].field_type +
//                 '</option>';
//         }
//         else{
//             select += '<option ' + '" value="' + data[i].id +  '">' +
//                 data[i].field_type +
//                 '</option>';
//         }
//     }
//     select += '</select>';
//     return select;
// }
