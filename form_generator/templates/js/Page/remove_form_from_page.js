function remove(_section){
    var ID = _section.split('_')[1];
    var sectionID = _section.split('_')[2];
    var formID = document.getElementById("form"+ID).getElementsByTagName("form").item(0).id;

    var xhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/page/1/" + formID + '/' + sectionID + '/';
    xhttp.open("DELETE", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json"); 
    xhttp.send(null);
    xhttp.onload = function () {
        if (xhttp.status == 200){
            window.location.reload();
        }
    };
}