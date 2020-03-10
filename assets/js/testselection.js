$(document).ready(function(){
    var dom = $('#testselection_div');
    $(dom).find('.js_back').unbind().bind('click',this,function(e){
        e.preventDefault();
        window.location.replace("/");
    });
    $(dom).find('.js_taketest').unbind().bind('click',this,function(e){
        var subjects = [];
        var i = 0;
        $(dom).find('.subject_select .subjects').each(function(index,obj){
            if($(this).find('input').prop("checked"))
            {
                subjects[i++] = $(this).find('input').val();
            }
        });
        window.location.replace("/testsetup/taketest?subjectids="+JSON.stringify(subjects));
        /*$.ajax({
            type    : "POST",
            url     : '/ajax/request',
            dataType: 'json',
            data: {
              'mode'             :'testsetup',
              'ack'              :'taketest',
              'subjectid'        :JSON.stringify(subjects),
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
        });*/

        console.log(subjects);
    });

});