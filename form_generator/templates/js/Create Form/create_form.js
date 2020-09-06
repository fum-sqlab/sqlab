/* 
    --------------------CREATE DYNAMIC FORM---------------------
    send_data() sends data to server-side for creating new form.
    ------------------------------------------------------------
 */

function send_data(){
    var form_title = document.getElementById("title").value;
    var form_desc = document.getElementById("description").value;
    var form_enable =  get_value("enable-f");
    var form_visible =  get_value("visible-f");
    var fields = get_field_data()
    var form ={
        "title": form_title,
        "slug": "slug_"+ form_title.split(' ').join('_'),
        "visible": form_visible,
        "enable": form_enable,
        "description": form_desc,
        "fields": fields
    }
    console.log(JSON.stringify(form))
    var xhttp = new XMLHttpRequest();
    var data = JSON.stringify(form);
    xhttp.open("POST", "http://127.0.0.1:8000/form/", true);
    xhttp.setRequestHeader("Content-Type", "application/json"); 
    xhttp.send(data);
    xhttp.onload = function () {
        if (xhttp.status == 201){
          window.location.reload();
        }
    };
}

function get_field_data(){
    var table = document.getElementById("myTable");
    var rows_number = document.getElementsByTagName("tr").length;
    var fields = []
    var i = 1;
    for(i; i< rows_number ; i++){
        var obj = {}
        var type = table.rows[i].cells[1].children[0].textContent;
        obj = {
            "field_id" : table.rows[i].cells[1].children[0].id,
            "type" : type,
            "name" : table.rows[i].cells[2].children[0].value,
            "label" : table.rows[i].cells[3].children[0].value,
            "required" : get_value("required"),
            "visible" : get_value("visible"),
            "enable" : get_value("enable"),
            "description" : table.rows[i].cells[7].children[0].value,
            "placeHolder" : table.rows[i].cells[8].children[0].value,
            "default_value" : (type == "boolean") ? get_value("boolean").toString() : table.rows[i].cells[9].children[0].value,       
        }

        if(table.rows[i].cells[11].childElementCount != 0){
            obj["max_value"] = table.rows[i].cells[11].children[0].value; 
        }
        if(table.rows[i].cells[10].childElementCount != 0){
            if(type == "checkbox" || type == "radio"){
                var value = table.rows[i].cells[10].children[0].value;
                var sep = value.split(',');
                items = [];

                if (value[0] != null){
                    for(j=0; j<sep.length; j++){
                        obj_item = { "name" : sep[j]}
                        items.push(obj_item);
                    }
                }
                obj["items"] = items;
            }
            else {
                obj["min_value"] = table.rows[i].cells[10].children[0].value;
            }
        }
        fields.push(obj);
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