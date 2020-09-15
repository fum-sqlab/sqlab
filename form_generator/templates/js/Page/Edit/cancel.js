function cancel(){
    var cancel = '<div class="box1">' + 
                 '<img class="card-img-top" src="C:\\Users\\Sara\\Desktop\\Add.png" alt="Card image cap">' +
                 '<h3 class="title">Section</h3>' +
                 '<ul class="icon">' +
                 '<li><button onclick="get_all_forms()"><i class="fa fa-edit"></i></button></li>' +
                 '</ul></div></div>';
    document.getElementById("forms").innerHTML = cancel; 
}