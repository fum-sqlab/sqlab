var count = 0;
var id;
function get_type_value(slc){
    if (slc == "create") {
        count++;
        id = document.getElementsByTagName("option")[index].id;
    }
    else if(slc == 'edit'){
        var table = document.getElementById("myTable");
        count = table.rows.length;
        id = -1;
    }
    var index = document.getElementById("fields").selectedIndex;
    var type = document.getElementsByTagName("option")[index].value;
    create_field_table(type, id);
}

function create_field_table(fType, fId){
    var table = document.getElementById("myTable");
    var row = table.insertRow(count);

    var type = row.insertCell(0);
    var name = row.insertCell(1);
    var label = row.insertCell(2);
    var required = row.insertCell(3);
    var visible = row.insertCell(4);
    var enable = row.insertCell(5);
    var description = row.insertCell(6);
    var placeholder = row.insertCell(7);
    var default_value = row.insertCell(8);
    var min_value = row.insertCell(9);
    var max_value = row.insertCell(10);

    name.innerHTML = '<input id="name" type="text" placeholder="Name">';
    label.innerHTML = '<input id="label" type="text" placeholder="Lable">';
    type.innerHTML = '<label id="'+ fId +'">' + fType + '</lable>';
    required.innerHTML = '<input id="required" type="checkbox">';
    visible.innerHTML = '<input id="visible" type="checkbox" checked="checked">';
    enable.innerHTML = '<input id="enable" type="checkbox" checked="checked">';
    description.innerHTML = '<input id="desc" type="text" placeholder="Description">';

    switch(fType){
        case "text":
        case "textarea":
            value = text();
            min_value.innerHTML = value[0];
            max_value.innerHTML = value[1];
            default_value.innerHTML = value[2];
            break;

        case "number":
            value = number();
            min_value.innerHTML = value[0];
            max_value.innerHTML = value[1];
            default_value.innerHTML = value[2];
            break;
        
        case "date":
            value = date();
            min_value.innerHTML = value[0];
            max_value.innerHTML = value[1];
            default_value.innerHTML = value[2];
            break;

        case "time":
            value = time();
            min_value.innerHTML = value[0];
            max_value.innerHTML = value[1];
            default_value.innerHTML = value[2];
            break;

        case "datetime":
            value = datetime();
            min_value.innerHTML = value[0];
            max_value.innerHTML = value[1];
            default_value.innerHTML = value[2];
            break;

        case "file":
            default_value.innerHTML = '<input type="file" id="defv">';
            break;
        
        case "url":
            default_value.innerHTML = '<input type="url" id="defv" placeholder="https://example.com">';
            break;

        case "boolean":
            min_value.innerHTML = null;
            max_value.innerHTML = null;
            default_value.innerHTML = boolean();
            break;
        
        case "checkbox":
        case "radio":
            value = checkbox_item();
            min_value.innerHTML = value[1];
            max_value.innerHTML = null;
            default_value.innerHTML = value[0];
            break;
    }
    placeholder.innerHTML = '<input id="placeholder" type="number" min="1">';
}

function delete_row() {
    if(count != 0){
        document.getElementById("myTable").deleteRow(count);
        count--;
    }
    
}

function text(){
    return arr = [
        '<input id="min_value" type="number" min="1" placeholder="min character">',
        '<input id="max_value" type="number" min="1" placeholder="max character">',
        '<input id="defv" type="text">'
    ]
}

function number(){
    return arr = [
        '<input id="min_value" type="number" min="1" placeholder="min value">',
        '<input id="max_value" type="number" min="1" placeholder="max value">',
        '<input id="defv" type="number" min="1">'
    ]
}

function date(){
    return arr = [
        'Start:<input id="min_value" type="date">',
        'End:<input id="max_value" type="date">',
        '<input id="defv" type="date">'
    ]
}

function datetime(){
    return arr = [
        'Start:<input id="min_value" type="datetime-local">',
        'End:<input id="max_value" type="datetime-local">',
        '<input id="defv" type="datetime-local">'
    ]
}

function time(){
    return arr = [
        'Start:<input id="min_value" type="time">',
        'End:<input id="max_value" type="time">',
        '<input id="defv" type="time">'
    ]
}

function boolean(){
    return '<input type="radio" id="yes" name="boolean" value="true">' +
           '<label for="yes">Yes</label>' +
           '<input type="radio" id="no" name="boolean" value="false">' +
           '<label for="no">No</label>';
}

function checkbox_item(){
    return arr = [
        '<input id="item" type="text" placeholder="default item checked">',
        '<input id="items" type="text" placeholder="Item Names">',
    ]
}

    