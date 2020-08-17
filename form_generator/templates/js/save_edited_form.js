function localUpdateForm(){
    var form_id = document.getElementById("id").textContent;
    var form = get_form_content_values();
    console.log(JSON.stringify(form))
    var xhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/form/" + form_id + "/";
    var data = JSON.stringify(form)
    xhttp.open("PATCH", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json"); 
    xhttp.send(data);
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
    
    for(i=1; i<table.rows.length; i++){
        var obj = {}
        var id = parseInt(table.rows[i].cells[0].textContent);
        obj = {
            "name" : table.rows[i].cells[1].children[0].value,
            "label" : table.rows[i].cells[2].children[0].value,
            "required" : table.rows[i].cells[4].children[0].checked,
            "visible" : table.rows[i].cells[5].children[0].checked,
            "description" : table.rows[i].cells[6].children[0].value,
            "min_value" : table.rows[i].cells[7].children[0].value,
            "max_value" : table.rows[i].cells[8].children[0].value,
            "default_value" : table.rows[i].cells[9].children[0].value,
            "placeHolder" : table.rows[i].cells[10].children[0].value
        }  

        if(id != -1){
            obj["id"] = id;
            fields.push(obj);
        }
        else{
            add_specific_field(table,obj, i);    
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

function add_specific_field(table,field_info, row_index){
    var form_id = document.getElementById("id").textContent;
    var field_id = table.rows[row_index].cells[3].children[0].value;
    var data = JSON.stringify(field_info);
    var xmlhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/form/set_field/" + field_id + "/" + form_id + "/";
    xmlhttp.open("PUT", url, true);
    xmlhttp.setRequestHeader("Content-Type", "application/json"); 
    xmlhttp.send(data);
}