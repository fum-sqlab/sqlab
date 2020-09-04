function delete_field(id){
    var table = document.getElementById("myTable");
    var field_id = table.rows[id].cells.item(0).innerHTML;
    var xmlhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8000/form/remove_field/" + field_id + "/";
    xmlhttp.open("DELETE", url, true);
    xmlhttp.send(null);
    xmlhttp.onload = function () {
        if (xmlhttp.status == 204){
          window.location.reload();
        }
    };
}