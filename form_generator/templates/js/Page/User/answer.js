function answer(_id){
    var section = _id.split('_')[1];
    var form = document.getElementById("form"+section).getElementsByTagName("form").item(0);
    var form_id = form.id;
    var answers = []
    for(var i = 0; i<form.length; i++){
        input_id = form[i].id;
        tn = form[i].tagName;
        switch(tn){
            case "INPUT":
                var value = form[i].value;
                break;
            case "FIELDSET":
                var value = fieldset(form[i]);
                i += form[i].getElementsByTagName("input").length;
                break;
        }
        answer = {
            "form"  : form_id,
            "field" : input_id,
            "value" : value
        }
        value = "";
        answers.push(answer);
    }
    var xhttp = new XMLHttpRequest();
    var data = JSON.stringify(answers);
    xhttp.open("POST", "http://127.0.0.1:8000/submit/", true);
    xhttp.setRequestHeader("Content-Type", "application/json"); 
    xhttp.send(data);
    xhttp.onload = function () {
        if (xhttp.status == 201){
          window.location.reload();
        }
    };
}

function fieldset(fieldset){
    count = fieldset.getElementsByTagName("input").length;
    inputs = fieldset.getElementsByTagName("input");
    var cb = "";
    for(var j = 0; j<count; j++){
        type = inputs[0].type;
        if( type == "checkbox"){
            if( inputs[j].checked == true ) cb += inputs[j].value + ',';
        }
        else if( inputs[j].checked == true ) return inputs[j].value;
    }
    return cb.substring(0, cb.length-1);
}
