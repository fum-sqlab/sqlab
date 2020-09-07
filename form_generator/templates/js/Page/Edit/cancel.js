function cancel(_id){
    var ID = _id.split('_')[1];
    var cancel = '<div class="box1">' + 
                 '<img class="card-img-top" src="C:\\Users\\Sara\\Desktop\\Add.png" alt="Card image cap">' +
                 '<h3 class="title">Section '+ ID +'</h3>' +
                 '<ul class="icon">' +
                 '<li><button id="'+ ID +'" onclick="get_all_forms(this)"><i class="fa fa-edit"></i></button></li>' +
                 '</ul></div></div>';
    document.getElementById("form"+ID).innerHTML = cancel; 
}