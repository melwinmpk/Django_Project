$(document).ready(function(){
    var dom = $('#taketest_div');

    var subject_ids = JSON.parse(($(dom).attr('data-subjectIds')).replace(/'/g, '"'));
    var question_Ids = JSON.parse(($(dom).attr('data-questionids')).replace(/'/g, '"'));
    var currentquestionindex = 1,currentsubjectindex = 1 ;
    $(dom).find('.js-checkanswer').unbind().bind('click',this,function(e){
        var optionindex = 1;
        var count=1;
        $(this).closest(".QuestionOuterDiv").find(".OptionsOuterDiv").find(".option").each(function(index,obj){
            if($(this).find('input').prop("checked"))
            {
                console.log( $(this).find('input').val());
                optionindex = count;
            }
            else{
                count++;
            }
        });
        console.log(optionindex);
        var questionid = parseInt($(this).closest(".QuestionOuterDiv").attr('data-questionid'))

            $.ajax({
                type    : "POST",
                url     : '/ajax/request',
                dataType: 'json',
                data: {
                  'mode'              :'testsetup',
                  'ack'               :'checkanswer',
                  'questionid'        :questionid,
                  csrfmiddlewaretoken :$(dom).find('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                  if(data.status == "success")
                  {
                    if(data.data.Ans == optionindex)
                    {
                        alert("Right answer!"+optionindex);
                        console.log(question_Ids);
                        console.log(currentquestionindex);
                        loadNextQuestion(question_Ids[1][++currentquestionindex]);
                    }
                    else{
                        alert("Wrong answer!");
                        loadNextQuestion(question_Ids[1][++currentquestionindex]);
                    }
                  }
                  else
                  {
                    alert(data);
                  }
                }
            });

    });

    function loadNextQuestion(index) {
    $.ajax({
            type    : "POST",
            url     : '/ajax/request',
            dataType: 'json',
            data: {
              'mode'             :'testsetup',
              'ack'              :'getquestiondata',
              'questionid'       :index,
              csrfmiddlewaretoken:$(dom).find('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (data) {
              if(data.status == "success")
              {
                   alert("Subject Got Saved !");
              }
              else
              {
                alert(data);
              }
            }
        });
    }

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