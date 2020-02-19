$(document).ready(function(){
    var dom = $('#taketest_div');

    var subject_ids = 0, question_Ids = 0 , currentquestionindex = 0,currentsubjectindex = 0,currentsubjectid = 0  ;
    $.ajax({
        type    : "POST",
        url     : '/ajax/request',
        dataType: 'json',
        data: {
          'mode'             :'testsetup',
          'ack'              :'gettestquestionids',
          csrfmiddlewaretoken:$(dom).find('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
          if(data.status == "success")
          {
            subject_ids = JSON.parse(data.data.subjectids)
            question_Ids = data.data.QuestionIds
            currentsubjectid = parseInt(subject_ids[0])
          }
          else
          {
            alert(data);
          }
        }
    });
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
                        nextquestion();
                    }
                    else{
                        alert("Wrong answer!");
                        nextquestion();
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

    function nextquestion(){

        if(question_Ids[currentsubjectid].length > currentquestionindex)
        {
             loadNextQuestion(question_Ids[currentsubjectid][++currentquestionindex])
        }
        else if(subject_ids.length > currentsubjectindex ){
            alert(false) // end of the test
        }
        else{
            currentquestionindex = 0;
            currentsubjectid = parseInt(subject_ids[++currentsubjectindex])
            loadNextQuestion(question_Ids[++currentsubjectindex][currentquestionindex])
        }
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