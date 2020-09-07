function save(_id){
    var _section = _id.split("_")[1];
    var _form = document.getElementById("form"+_section).getElementsByTagName("form").item(0).id;
    var section = {
        "title" : "section"+ _section + _form,
        "slug" : "slug_1_" +  _section + "_" + _form,
        "placeholder" : _section
    };
    var xhttp = new XMLHttpRequest();
    var data = JSON.stringify(section)
    console.log(data)
    var url = "http://127.0.0.1:8000/page/1/" + _form + '/';
    xhttp.open("PUT", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json"); 
    xhttp.send(data);
    xhttp.onload = function () {
        if (xhttp.status == 200){
            window.location.reload();
        }
    };
}