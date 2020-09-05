function localUpdateForm(){
    var form_id = document.getElementById("id").textContent;
    var form = get_form_content_values();
    var xhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/form/" + form_id + "/";
    var data = JSON.stringify(form)
    xhttp.open("PATCH", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json"); 
    xhttp.send(data);
    xhttp.onload = function () {
        if (xhttp.status == 200){
          window.location.reload();
        }
    };
}

function get_form_content_values(){
    var form_title =  document.getElementById("title").value;
    var form_desc = document.getElementById("description").value;
    var form_enable = get_value("enable-f");
    var form_visible = get_value("visible-f");
    var fields = get_field_row_table_cotent();
    var form ={
        "title": form_title,
        "visible": form_visible,
        "enable": form_enable,
        "description": form_desc,
        "fields" : fields
    }
    return form;
}

function get_field_row_table_cotent(){
    var table = document.getElementById("myTable");
    var fields = []
    var lng = table.rows.length;
    var i = 1;
    for(i; i<lng ;i++){
        var obj = {}
        var id = parseInt(table.rows[i].cells[0].textContent);
        var type = table.rows[i].cells[1].children[0].textContent;
        obj = {
            "name" : table.rows[i].cells[2].children[0].value,
            "label" : table.rows[i].cells[3].children[0].value,
            "required" : table.rows[i].cells[4].children[0].checked,
            "visible" : table.rows[i].cells[5].children[0].checked,
            "enable" : table.rows[i].cells[6].children[0].checked,
            "description" : table.rows[i].cells[7].children[0].value,
            "placeHolder" : table.rows[i].cells[8].children[0].value,
            "default_value" : (type == "boolean") ? get_value("boolean").toString() : table.rows[i].cells[9].children[0].value,
        }  
        if(table.rows[i].cells[11].childElementCount != 0){
            obj["max_value"] = table.rows[i].cells[11].children[0].value; 
        }
        if( id != -1 ){
            // When Field Exist in datbase
            if(table.rows[i].cells[10].childElementCount != 0){
                if(type == "checkbox" || type == "radio"){
                    var value = table.rows[i].cells[10].children[0].value.split(',');
                    var ids = table.rows[i].cells[10].children[0].id.split(',');
                    var lngV = value.length;
                    var lngI = ids.length;
                    items = [];
                    if( value[0] != "" || ids[0] != ""){
                        for(k=0; k<lngI || k<lngV; k++){
                            var val = (k >= lngV || value[0]=="") ? null : value[k];
                            if(k >= lngI || ids[0]==""){
                                add_choice(id, val)
                            }
                            else{
                                obj_item = { "id": ids[k], "name": val}
                                items.push(obj_item);
                            }
                        }
                    }
                    obj["items"] = items;
                }
                else{
                    obj["min_value"] = table.rows[i].cells[10].children[0].value; 
                }
            }
            obj["id"] = id;
            fields.push(obj);           
        }
        if( id == -1 ){
            //When you want to create new field
            if(table.rows[i].cells[10].childElementCount != 0){
                if( type != "checkbox" && type != "radio" ){
                    obj["min_value"] = table.rows[i].cells[10].children[0].value;
                }
                else{
                    var value = table.rows[i].cells[10].children[0].value.split(',');
                    var lngV = value.length;
                    items = [];
                    var j = 0;
                    for(j; j<lngV; j++){
                        obj_item = {"name": value[j]}
                        items.push(obj_item);
                    }
                    obj["items"] = items;
                }
            }
            add_specific_field(table, obj, i);
        }
    }
    return fields;
}

function get_value(element_id){
    var checkBox = document.getElementById(element_id);
    if (checkBox.checked == true){
        return true;
    }
    return false;
}

function add_specific_field(table, field_info, row_index){
    var form_id = document.getElementById("id").textContent;
    var field_id = table.rows[row_index].cells[1].children[0].id;
    var data = JSON.stringify(field_info);
    var xmlhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/form/set_field/" + field_id + "/" + form_id + "/";
    xmlhttp.open("PUT", url, true);
    xmlhttp.setRequestHeader("Content-Type", "application/json"); 
    xmlhttp.send(data);
}

function add_choice(field_id, name){
    obj = {
        "field" : field_id,
        "name" : name
    }
    console.log(obj)
    var data = JSON.stringify(obj);
    var xmlhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/choice/";
    xmlhttp.open("POST", url, true);
    xmlhttp.setRequestHeader("Content-Type", "application/json"); 
    xmlhttp.send(data);
}