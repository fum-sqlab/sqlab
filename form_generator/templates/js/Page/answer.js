function answering(_id){
    var form = document.getElementsByTagName("form").item(0);
    var form_id = form.id;
    var answers = []
    var file_id = []
    for(var i = 0; i<form.length; i++){
        input_id = form[i].id;
        tn = form[i].tagName;
        switch(tn){
            case "INPUT":
            case "TEXTAREA":
                if(form[i].type == "file"){
                    file_id.push(i);
                }
                else{
                    var value = form[i].value;
                }
                var type = form[i].type;
                break;
            case "FIELDSET":
                var value = fieldset(form[i]);
                var type = "fieldSet";
                i += form[i].getElementsByTagName("input").length;
                break;
        }
        // if (value != "" && form[i].type != "file") {
        //     answer = {
        //         "form"  : form_id,
        //         "field" : input_id,
        //         "value" : value,
        //         "type"  : type
        //     }
        //     answers.push(answer);
        // }
        if (form[i].type != "file") {
            answer = {
                "form"  : form_id,
                "field" : input_id,
                "value" : value,
                "type"  : type
            }
            answers.push(answer);
        }
        value = "";
        type = "";
    }
    set_ans = {
        "id" : 1,
        "answers" : answers
    }
    var xhttp = new XMLHttpRequest();
    var data = JSON.stringify(set_ans);
    console.log(data)
    xhttp.open("POST", "http://127.0.0.1:8000/submit/", true);
    xhttp.setRequestHeader("Content-Type", "application/json"); 
    xhttp.send(data);
    xhttp.onload = function () {
        if (xhttp.status == 200){
            res = xhttp.response.split(":")[1]
            sub_id = res.substring(0, res.length - 1)
            for(var x = 0; x<file_id.length; x++){
                send_file(form[file_id[x]], sub_id, form_id, form[file_id[x]].id);
            }
            document.getElementById("forms").innerHTML = back_to_show_ans(form_id);
        }else if(xhttp.status == 400 || xhttp.status == 404){
            console.log(xhttp.response)
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
function send_file(fileinput, _sub_id, _form_id, _field_id){
    var FD = new FormData();
    FD.append("file", fileinput.files[0]);
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:8000/file/" + _field_id + "/" + _form_id + "/" + _sub_id + "/", true);
    xhttp.send(FD);
    xhttp.onload = function () {
        if (xhttp.status == 400){
            console.log(xhttp.response)
        }
    };
}