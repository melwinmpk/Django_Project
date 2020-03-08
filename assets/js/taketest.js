$(document).ready(function(){
    var dom = $('#taketest_div');
    var subject_ids = 0, question_Ids = 0 , currentquestionindex = 0,currentsubjectindex = 0,currentsubjectid = 0,totalscore = 0,attempted = 0,Subjectdata = {}  ;
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
            console.log(data.data.Subjectdata);
            console.log(data.data.QuestionTypes);
            QuestionTypes = data.data.QuestionTypes;
            Subjectdata = data.data.Subjectdata;
          }
          else
          {
            alert(data);
          }
        }
    });

    bindevents();

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
                loadquestion(data.data);
//                   alert("Subject Got Saved !");
              }
              else
              {
                alert(data);
              }
            }
        });
    }

    function nextquestion(){
        console.log("currentsubjectid=>",currentsubjectid);
        console.log("currentquestionindex=>",currentquestionindex);
        console.log("question_Ids[currentsubjectid]=>",question_Ids[currentsubjectid]);
        console.log("subject_ids=>",subject_ids);
        console.log("currentsubjectindex=>",currentsubjectindex);
        console.log("question_Ids=>",question_Ids);
        if(question_Ids[currentsubjectid].length - 1 > currentquestionindex)
        {
             loadNextQuestion(question_Ids[currentsubjectid][++currentquestionindex])
        }
        else if(subject_ids.length - 1 <= currentsubjectindex ){
             // end of the test
            $(dom).find('.result').find('.score').html(totalscore);
            $(dom).find('.result').find('.attempted').html(attempted);
            alert("Your final score is =>"+totalscore+"/"+attempted);
            window.history.back();
            return false;
        }
        else{
            currentquestionindex = 0;
            currentsubjectid = parseInt(subject_ids[++currentsubjectindex])
            loadNextQuestion(question_Ids[currentsubjectid][currentquestionindex])
        }
    }
    function loadquestion(data){
        var questionouterdiv = $(dom).find('.QuestionOuterDiv');
        var html_data = '';
        if(data.QuestionTypeId_id == 1)
        {
            html_data = loadmcqhtml(data)
        }
//        $(dom).
        $(dom).find('.QuestionOuterDiv').html(html_data);
        bindevents();
    }
    function loadmcqhtml(data){
        var html = ''
        html = '<div>'+
                    '<span>Question Type:<span>'+QuestionTypes[data.QuestionTypeId_id]['QuestionType']+'</span></span>'+
                    '<span>Subject:<span>'+Subjectdata[data.SubjectId_id]['SubjectName']+'</span></span>'+
                '</div>'+
                '<div class="Question">'+
                    data.Question+
                '</div>'+
                '<div class="OptionsOuterDiv">';
                var options = JSON.parse(data.Options);
                for(option in options)
                {
                    html += '<div class="option">'+
                                '<input type="radio" name="option_radio" value="'+options[option]+'">'+
                                '<span>'+options[option]+'</span>'+
                            '</div>';
                }


     html +=    '</div>'+
                '<div>'+
                    '<button class="js-checkanswer">Save</button>'+
                '</div>';

     html =            '<div class="dquizquestion">'+
                            data.Question+
                        '</div>'+
                        '<div class = "OptionsOuterDiv">';
                        var options = JSON.parse(data.Options);
                        for (option in options)
                        {
     html +=                '<label class="quizlabel no_hover js-checkanswer">'+
                                '<input type="radio" class="radioButton" name="undefined+639770" value="'+option+'">'+
                                '<div class="labelDiv container">'+
                                    '<div class="option_msg">'+
                                        '<div class="radioText">'+
                                            option+
                                        '</div>'+
                                        '<div class="indicator"></div>'
                                    '</div>'+
                                '</div>'+
                            '</label>';
                        }
     html +=            '</div>';
     return html;
    }
    function bindevents()
    {
        $(dom).find('.marks').find('.score').html(totalscore);
        $(dom).find('.marks').find('.attempted').html(attempted);
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
                            totalscore++;
                            attempted++;
                            nextquestion();
                        }
                        else{
                            attempted++;
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
    }


});