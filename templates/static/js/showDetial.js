$('.exam_quest').bind("click",function () {
                    $('.detial').css({
                        display:'block'
                    })
                });

$('.cancel').bind("click",function () {
                    $('.detial').css({
                        display:'none'
                    })
                });
var a = setInterval(function(){
    if(document.getElementById('exam').scrollTop >= document.getElementById('exam').scrollHeight*0.2 ){
        change_arrow('.up','.down');
    }
    else{
        change_arrow('.down','.up');
        console.log(document.getElementById('exam').scrollTop+' '+document.getElementById('exam').scrollHeight*0.2);
    }
},500);

function change_arrow(id1,id2){
    $(id1).css({
            display:'block'
    })
    console.log($(id1));
    $(id2).css({
            display:'none'
    })
}
