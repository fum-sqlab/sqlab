/* 
    -------------CREATE DYNAMIC FORM---------------
    loadFieldContet() fetches fields from database.
    add_row() creates new row of field for form.
    delete_row() deletes the last row of field table.
    -----------------------------------------------
 */
function loadFieldContent(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var myObj = JSON.parse(this.responseText);
            // table = add_row(myObj);
            document.getElementById("fields").innerHTML = make_selector_field(myObj);
        }
    };
    var url = "http://127.0.0.1:8000/field/";
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}
function delete_row() {
    document.getElementById("myTable").deleteRow(1);
}

function make_selector_field(data){
    var select;
    for(i=0; i<data.length; i++){
        select += '<option ' + '" value="' + data[i].field_type +  '" id="' + data[i].id + '">' +
                data[i].field_type +
                '</option>';
    }
    return select;
}