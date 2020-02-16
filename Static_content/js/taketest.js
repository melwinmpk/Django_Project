$(document).ready(function(){
    var dom = $('#taketest_div');

    var subject_ids = JSON.parse(($(dom).attr('data-subjectIds')).replace(/'/g, '"'));
    var question_Ids = JSON.parse(($(dom).attr('data-questionids')).replace(/'/g, '"'));

    console.log(subject_ids)
    console.log(question_Ids)
    $(dom).find('.js-checkanswer').unbind().bind('click',this,function(e){
        var optionindex = 1;
        var count=1;
        $(this).closest(".QuestionOuterDiv").find(".OptionsOuterDiv").find(".option").each(function(index,obj){
            if($(this).find('input').prop("checked"))
            {
                console.log( $(this).find('input').val());
                console.log(optionindex = count);
            }
            else{
                count++;
            }
        });
        console.log(optionindex);

    });

//    $.ajax({
//            type    : "POST",
//            url     : '/ajax/request',
//            dataType: 'json',
//            data: {
//              'mode'             :'testsetup',
//              'ack'              :'taketest',
//              'subjectid'        :JSON.stringify(subjects),
//              csrfmiddlewaretoken:$(dom).find('input[name=csrfmiddlewaretoken]').val()
//            },
//            success: function (data) {
//              if(data.status == "success")
//              {
//                   alert("Subject Got Saved !");
//              }
//              else
//              {
//                alert(data);
//              }
//            }
//        });

//    .attr(

});
//