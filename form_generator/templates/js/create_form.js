/* 
    -------------CREATE DYNAMIC FORM---------------
    loadFieldContet() fetches fields from database.
    add_row() creates new row of field for form.
    delete_row() deletes the last row of field table.
    -----------------------------------------------
 */
function loadFieldContent(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var myObj = JSON.parse(this.responseText);
            table = add_row(myObj)
        }
    };
    var url = "http://127.0.0.1:8000/field/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}
function delete_row() {
    document.getElementById("myTable").deleteRow(1);
}

function add_row(data) {
    var table = document.getElementById("myTable");
    var row = table.insertRow(1);
    var name = row.insertCell(0);
    var label = row.insertCell(1);
    var type = row.insertCell(2);
    var required = row.insertCell(3);
    var visible = row.insertCell(4);
    var enable = row.insertCell(5);
    var description = row.insertCell(6);
    var min_value = row.insertCell(7);
    var max_value = row.insertCell(8);
    var default_value = row.insertCell(9);
    var placeholder = row.insertCell(10);

    name.innerHTML = '<input id="name" type="text">';
    label.innerHTML = '<input id="label" type="text">';
    type.innerHTML = make_selector_field(data);
    required.innerHTML = '<input id="required" type="checkbox">';
    visible.innerHTML = '<input id="visible" type="checkbox" checked="checked">';
    enable.innerHTML = '<input id="enable" type="checkbox" checked="checked">'
    description.innerHTML = '<input id="desc" type="text">';
    min_value.innerHTML = '<input id="minv" type="text">';
    max_value.innerHTML = '<input id="maxv" type="text">';
    default_value.innerHTML = '<input id="defv" type="text">';
    placeholder.innerHTML = '<input id="palceholder" type="text">';

}

function make_selector_field(data){
    select = '<select id="field" name="field">';
    for(i=0; i<data.length; i++){
        select += '<option ' + '" value="' + data[i].id +  '">' +
                data[i].field_type +
                '</option>';
    }
    select += '</select>';
    return select;
}

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
    
    var xhttp = new XMLHttpRequest();
    var data = JSON.stringify(form)
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
    for(i=1; i< rows_number ; i++){
        var obj = {}
        obj = {
            "name" : table.rows[i].cells[0].children[0].value,
            "label" : table.rows[i].cells[1].children[0].value,
            "field_id" : table.rows[1].cells[2].children[0].value,
            "required" : get_value("required"),
            "visible" : get_value("visible"),
            "description" : table.rows[i].cells[5].children[0].value,
            "min_value" : table.rows[i].cells[6].children[0].value,
            "max_value" : table.rows[i].cells[7].children[0].value,
            "default_value" : table.rows[i].cells[8].children[0].value,
            "placeHolder" : table.rows[i].cells[9].children[0].value
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