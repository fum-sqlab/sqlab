function loadGroups(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var myObj = JSON.parse(this.responseText);
            create_selector(myObj)
        }
    };
    var url = "http://127.0.0.1:8000/group/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function create_selector(data){
    var text = '<label>Group</label>';
    text += '<select name="gp" id="gp" multiple>';
    for(i=0; i<data.length; i++){
        text += '<option id="'+ data[i].id + '">' + data[i].gp_name + '</option>';
    }
    text += '</select>';
    document.getElementById("group").innerHTML = text;
}