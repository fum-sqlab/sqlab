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

function form(data){
    document.getElementById("ID").innerHTML = '<label id="id">' + data.id + '</label>';
    document.getElementById("Title").innerHTML = '<input type="text" id="title" name="title" value="'
                                                 + data.title
                                                 + '">';
    document.getElementById("Description").innerHTML = '<textarea type="text" id="description" name="description"'
                                                       + '" style="height:200px">'+ data.description +'</textarea>';
    document.getElementById("checkboxes").innerHTML = checkbox_check_l(data.enable , "enable") +
                                                      checkbox_check_l(data.visible, "visible");

    
    var i=0;                                                
    for(i; i<data.fields.length; i++){
        field(data.fields, i);
    }
    
}

function field(fields, index){

    var table = document.getElementById("myTable");  
    var row = table.insertRow(index+1);
    var id = row.insertCell(0);
    var type = row.insertCell(1);
    var name = row.insertCell(2);
    var label = row.insertCell(3);
    var required = row.insertCell(4);
    var visible = row.insertCell(5);
    var enable = row.insertCell(6);
    var description = row.insertCell(7);
    var placeholder = row.insertCell(8);
    var default_value = row.insertCell(9);
    var min_value = row.insertCell(10);
    var max_value = row.insertCell(11);
    var deleted = row.insertCell(12);

    id.innerHTML = fields[index].id; 
    name.innerHTML = '<input id="name" type="text" value="' + fields[index].name + '">';
    label.innerHTML = '<input id="label" type="text" value="' + fields[index].label + '">';
    type.innerHTML = '<label>' + fields[index].field_type + '</label>';
    required.innerHTML = checkbox_check_nl(fields[index].required, "required", fields[index].id);
    visible.innerHTML = checkbox_check_nl(fields[index].visible, "visible", fields[index].id);
    enable.innerHTML = checkbox_check_nl(fields[index].enable, "enable", fields[index].id);
    description.innerHTML = '<input id="desc" type="text" value="' + fields[index].description + '">';
    placeholder.innerHTML = '<input id="placeholder" type="number" value="' + fields[index].placeHolder + '">';
    deleted.innerHTML = '<button class="w3-button w3-red w3-padding-small" onclick="helper(this)">-</button>';
    id.style.display = "none";

    var min = fields[index].min_value;
    var max = fields[index].max_value;
    var defv = fields[index].default_value;

    switch(fields[index].field_type){
        case "text":
        case "textarea":
            value = _text(min, max, defv);
            min_value.innerHTML = value[0];
            max_value.innerHTML = value[1];
            default_value.innerHTML = value[2];
            break;

        case "number":
            value = _number(min, max, defv);
            min_value.innerHTML = value[0];
            max_value.innerHTML = value[1];
            default_value.innerHTML = value[2];
            break;
        
        case "date":
            value = _date(min, max, defv);
            min_value.innerHTML = value[0];
            max_value.innerHTML = value[1];
            default_value.innerHTML = value[2];
            break;

        case "time":
            value = _time(min, max, defv);
            min_value.innerHTML = value[0];
            max_value.innerHTML = value[1];
            default_value.innerHTML = value[2];
            break;

        case "datetime":
            value = _datetime(min, max, defv);
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
            default_value.innerHTML = _boolean(defv);
            break;
        
        case "checkbox":
        case "radio":
            value = _checkbox_item(defv, fields[index].items);
            min_value.innerHTML = value[1];
            max_value.innerHTML = null;
            default_value.innerHTML = value[0];
            break;
    }
}

function checkbox_check_nl(data, type, id){
    if(data == true){
        return '<input id="'+ type + '-' + id + '" type="checkbox" checked="checked">'
    }
    else{
        return '<input id="'+ type + '-' + id + '" type="checkbox">'
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

function _text(min, max, defv){
    return arr = [
        '<input id="min_value" type="number" value="' + min + '" placeholder="min charcter">',
        '<input id="max_value" type="number" value="' + max + '" placeholder="max charcter">',
        '<input id="defv" type="text" value="' + defv + '">'
    ]
}

function _number(min,  max, defv){
    return arr = [
        '<input id="min_value" type="number" value="' + min + '" placeholder="min number">',
        '<input id="max_value" type="number" value="' + max + '" placeholder="max number">',
        '<input id="defv" type="number" value="' + defv + '">'
    ]
}

function _date(min,  max, defv){
    return arr = [
        'Start:<input id="min_value" type="date" value="' + min + '">',
        'End:<input id="max_value" type="date" value="' + max + '">',
        '<input id="defv" type="date" value="' + defv + '">'
    ]
}

function _datetime(min,  max, defv){
    return arr = [
        'Start:<input id="min_value" type="datetime-local" value="' + min + '">',
        'End:<input id="max_value" type="datetime-local" value="' + max + '">',
        '<input id="defv" type="datetime-local" value="' + defv + '">'
    ]
}

function _time(min,  max, defv){
    return arr = [
        'Start:<input id="min_value" type="time" value="' + min + '">',
        'End:<input id="max_value" type="time" value="' + max + '">',
        '<input id="defv" type="time" value="' + defv + '">'
    ]
}

function _boolean(defv){
    if( defv == "true" ){
        return '<input type="checkbox" id="boolean" name="boolean" checked>';
    }
    else{
        return '<input type="checkbox" id="boolean" name="boolean">';
    }
    
}

function _checkbox_item(defv, items){
    var str_items ='';
    var ids = '';
    for(j=0; j<items.length; j++){
        str_items += items[j].name + ',';
        ids += items[j].id + ',';
    }
    str_items = str_items.substring(0, str_items.length-1)
    ids = ids.substring(0, ids.length-1)
    return arr = [
        '<input id="defv" type="text" value="' + defv + '" placeholder="Default Item">',
        '<input id="'+ ids +'" type="text" value="' + str_items + '" placeholder="Item Names">'
    ]
}
