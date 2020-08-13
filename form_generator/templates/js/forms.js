function loadForms() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          var all_forms = JSON.parse(this.responseText);
          return create_list(all_forms);
          
      }
    };
    xhttp.open("GET", "http://127.0.0.1:8000/form/", true);
    xhttp.send(null);
}

function create_list(data) {
    var table="<tr><th>ID</th><th>Title</th></tr>";
    for (i = 0; i <data.length; i++) { 
      table +=    "<tr><td>" +
                      data[i].id +
                  "</td><td>" +
                      data[i].title +
                  "</td></tr>";
    }
    document.getElementById("form_table").innerHTML = table;
    return table;
}