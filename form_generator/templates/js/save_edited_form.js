function localUpdateForm(){
    var form_id = document.getElementById("id").textContent;
    form = get_form_content_values();
    
    var xhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/form/" + form_id + "/";
    var data = JSON.stringify(form)
    xhttp.open("PATCH", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json"); 
    xhttp.send(data);
}

function get_value(element_id){
    var checkBox = document.getElementById(element_id);
    if (checkBox.checked == true){
        return true;
    }
    return false;
}

function get_form_content_values(){
    var form_title =  document.getElementById("title").value;
    var form_desc = document.getElementById("description").value;
    var form_enable = get_value("enable-f");
    var form_visible = get_value("visible-f");
    var fields = get_field_row_table_cotent();
    var form ={
        "title": form_title,
        "slug": "slug_1",
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
            "id" : id,
            "name" : table.rows[i].cells[1].children[0].value,
            "label" : table.rows[i].cells[2].children[0].value,
            "required" : get_value("required-" + id),
            "visible" : get_value("visible-" + id),
            "description" : table.rows[i].cells[6].children[0].value,
            "min_value" : table.rows[i].cells[7].children[0].value,
            "max_value" : table.rows[i].cells[8].children[0].value,
            "default_value" : table.rows[i].cells[9].children[0].value,
            "placeHolder" : table.rows[i].cells[10].children[0].value
        }    
        fields.push(obj);
    }
    return fields;
}