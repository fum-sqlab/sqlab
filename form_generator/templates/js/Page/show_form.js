function set(_id){
    var ID = _id.split('_')[1];
    var selectID = document.getElementById("select"+ID).selectedIndex;
    var formID = document.getElementsByTagName("option")[selectID].id;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var objForm = JSON.parse(this.responseText);
        document.getElementById("form"+ID).innerHTML = form(objForm, ID, 1);
      }
    };
    var url = "http://127.0.0.1:8000/form/" + formID + "/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function show(type){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var objForm = JSON.parse(this.responseText);
        seperator_form(objForm, type);
      }
    };
    var url = "http://127.0.0.1:8000/page/1/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function seperator_form(data, type){
    var code = ( type == "edit" ) ? 2 : 3; 
    forms = data.forms;
    for(var index = 0; index < forms.length; index++){
        var location = forms[index].section;
        for(var loc = 0; loc < location.length; loc++){
            document.getElementById("form"+location[loc].placeholder).innerHTML = form(forms[index], location[loc], code);
        }
    }
}

function form(data, _id, method_code){

    var text = '<section class="align-items-center">';
    text += '<h2 class="h1-responsive font-weight-bold text-center my-4">'+ data.title +'</h2>';
    text += '<p class="text-center w-responsive mx-auto mb-5">'+ data.description +'</p><hr>';
    text += '<div class="row">';
    text += '<div class="col-md-12">';
    text += '<form id="'+ data.id +'" class="p-2">';

    _field = sort(data.fields);
    for(var i = 0; i< _field.length; i++){
        type = _field[i].field_type;
        switch(type){
            case "file":
                text += fileF(_field[i]);
                break;
            case "textarea":
                text += textareaF(_field[i]);
                break;
            case "text":
                text += textF(_field[i]);
                break;
            case "checkbox":
                text += checkboxF(_field[i]);
                break;
            case "radio":
                text += radioF(_field[i]);
                break;
            case "time":
            case "date":
            case "datetime":
              text += date_time(_field[i]);
              break;
            default:
              text += similar_field(_field[i]);
              break;
        }
    }
    text += '</form>';
    if( method_code == 1){
        text += '<div class="m-2 text-center text-md-center">' +
                '<button id="ss_'+ _id +'" class="btn btn-success" onclick="save(this.id)">Save</button>' + 
                '<button id="cc_'+ _id +'" class="btn btn-danger" onclick="cancel(this.id)">cancle</button>' +          
                '</div><div class="status"></div></div></div>';
    }
    else if(method_code == 2){
        text += '<div class="m-2 text-center text-md-center">' +
                '<button id="r_'+ _id.placeholder + "_" + _id.id +'" class="btn btn-danger" onclick="remove(this.id)">Remove</button>' +        
                '</div><div class="status"></div></div></div>';
    }
    else{
        text += '<div class="m-2 text-center text-md-center">' +
                '<button id="sa_" class="btn btn-primary" onclick="answer(this.id)">Set Answwer</button>' +        
                '</div><div class="status"></div></div></div>';
    }
    
    return text;
}

function fileF(data){
    var disable = disableF(data.enable);
    var visible = visibleF(data.visible);
    var file = '<div class="form-group row">';
    file += '<label class="col-sm-2 col-form-label" for="'+ data.id +'"' + visible + disable +'>'+ data.label +'</label>';
    file += '<div class="col-sm-10">';
    file += '<input type="file" class="form-control-file" id="'+ data.id +'"'+ visible + disable +'>';
    file += '</div></div>';
    return file;
}
function textareaF(data){
    var disable = disableF(data.enable);
    var visible = visibleF(data.visible);
    var text = '<div class="form-group row">';
    text += '<label class="col-sm-2 col-form-label" for="'+ data.id +'"'+ visible +'>'+ data.label +'</label>';
    text += '<div class="col-sm-10">';
    text += '<textarea class="form-control" id="'+ data.id +'" name="'+ data.name +'" rows="3"'+ visible + disable +'></textarea>';
    text += '</div></div>';
    return text;
}
function textF(data){
    var disable = disableF(data.enable);
    var visible = visibleF(data.visible);
    var text = '<div class="form-group row">';
    text += '<label class="col-sm-2 col-form-label" for="'+ data.id +'">'+ data.label + visible +'</label>';
    text += '<div class="col-sm-10">';
    text += '<input type="text" class="form-control" id="'+ data.id + '"'+ visible + disable +'>';
    text += '</div></div>';
    return text;
}
function checkboxF(data){
    var items = data.items;
    var default_val = data.default_value;
    var disable = disableF(data.enable);
    var visible = visibleF(data.visible);
    var cb = '<fieldset class="form-group" id="' + data.id + '"' + visible + disable + '>';
    cb += '<div class="row">';
    cb += '<legend  class="col-form-label col-sm-2 pt-0">' + data.label + '</legend>';
    cb += '<div class="col-sm-10">';
    for(var j = 0; j < items.length; j++){
        cb += ' <div class="form-check">';
        cb += '<input class="form-check-input" type="checkbox"'+
              'value="' + items[j].name + '"'+
              'id="'+ items[j].id +'">';
        cb += '<label class="form-check-label" for="' + items[j].id + '">' + items[j].name + '</label>';
        cb += '</div>';
    }
    cb += '</fieldset>';
    return cb;
}
function radioF(data){
    var items = data.items;
    var default_val = data.default_value;
    var disable = disableF(data.enable);
    var visible = visibleF(data.visible);
    var cb = '<fieldset class="form-group" id="' + data.id + '"' + visible + disable + '>';
    cb += '<div class="row">';
    cb += '<legend  class="col-form-label col-sm-2 pt-0">' + data.label + '</legend>';
    cb += '<div class="col-sm-10">';
    for(var k = 0; k < items.length; k++){   
        cb += ' <div class="form-check">';
        cb += '<input class="form-check-input" type="radio"'+
              'name="' + data.name + '"'+
              'id="'+ items[k].id +'">';
        cb += '<label class="form-check-label" for="' + items[k].id + '">' + items[k].name + '</label>';
        cb += '</div>';
    }
    cb += '</div></fieldset>';
    return cb;
}
function date_time(data){
    var disable = disableF(data.enable);
    var visible = visibleF(data.visible);
    var type = data.field_type;
    if (type == "datetime"){
      type = "datetime-local";
    }
    var datetime = '<div class="form-group row">';
    datetime += '<label class="col-sm-2 col-form-label" for="'+ data.id +'"'+ visible +'>'+ data.label+'</label>';
    datetime += '<div class="col-sm-10">';
    datetime += '<input type="'+ type +'" class="form-control" id="'+ data.id + '"'+
                 visible + disable + '>';
    datetime += '</div></div>';
    return datetime;
}
function similar_field(data){
  var disable = disableF(data.enable);
  var visible = visibleF(data.visible);
  var similar = '<div class="form-group row">';
  similar += '<label class="col-sm-2 col-form-label" for="'+ data.id +'"'+ visible +'>'+ data.label +'</label>';
  similar += '<div class="col-sm-10">';
  similar += '<input type="'+ data.field_type +'" class="form-control" id="'+ data.id + '"'+ visible + disable +'>';
  similar += '</div></div>';
  return similar;
}
/* ------------------------------------------------------------------------------------------------------------------------------- */
function sort(data_list){
    for(b=0; b<data_list.length; b++){
      for(c=b+1; c<data_list.length; c++){
        if(data_list[b].placeHolder > data_list[c].placeHolder){
          dd = data_list[b];
          data_list[b] = data_list[c];
          data_list[c] = dd;
        }
      }
    }
    return data_list;
}
function disableF(data){
    return (data == false) ? "disabled" : "";
}
function visibleF(data){
    return (data ==false) ? 'style="display: none;"' : '';
}
/* ------------------------------------------------------------------------------------------------------------------------------- */

