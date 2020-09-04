function delete_new_row() {
    var table = document.getElementById("myTable");
    var lng = table.rows.length;
    
    var field_id = table.rows[lng-1].cells[0].textContent;
    if(field_id == -1){
        document.getElementById("myTable").deleteRow(lng-1);
    }      
}
    