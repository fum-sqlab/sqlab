function localFieldContent(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var myObj = JSON.parse(this.responseText);
            table = create_field_table(myObj)
        }
    };
    var url = "http://127.0.0.1:8000/field/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function create_field_table(data) {
    var table = document.getElementById("myTable");
    var lng = table.rows.length;
    var row = table.insertRow(lng);
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

    id.innerHTML = -1;
    name.innerHTML = '<input id="name" type="text">';
    label.innerHTML = '<input id="label" type="text">';
    type.innerHTML = make_selector_field(data);
    required.innerHTML = '<input id="required" type="checkbox">';
    visible.innerHTML = '<input id="visible" type="checkbox" checked>';
    enable.innerHTML = '<input id="enable" type="checkbox" checked>';
    description.innerHTML = '<input id="desc" type="text">';
    min_value.innerHTML = '<input id="minv" type="text">';
    max_value.innerHTML = '<input id="maxv" type="text">';
    default_value.innerHTML = '<input id="defv" type="text">';
    placeholder.innerHTML = '<input id="palceholder" type="text">';

    id.style.display = "none";
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
