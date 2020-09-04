function delete_new_row() {
    var table = document.getElementById("myTable");
    var lng = table.rows.length;
    if(table.rows[lng-1].cells[0].childElementCount != 0){
        var field_id = table.rows[lng-1].cells[0].children[0].id;
        if(field_id == -1){
            document.getElementById("myTable").deleteRow(lng-1);
        }
    }
       
}
    