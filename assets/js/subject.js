$(document).ready(function(){
  var dom = $('#subject_div');
  $(dom).find('.subject_form').find('.savesubject_button').unbind().bind('click',this,function(e){
    var subjectname = $(this).closest('.subject_form').find('.js_subjectname').val();
    e.preventDefault();
    $.ajax({
        type    : "POST",
        url     : '/ajax/request',
        dataType: 'json',
        data: {
          'mode'             :'testsetup',
          'ack'              :'savesubject',
          'subjectname'      :subjectname,
          csrfmiddlewaretoken:$(dom).find(".subject_form").find('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
          if(data.status == "success")
          {
               alert("Subject Got Saved !");
               window.location.replace("/");
          }
          else
          {
            alert(data);
          }
        }
    });
  });
  $(dom).find('.subject_form').find('.js_back').unbind().bind('click',this,function(e){
    e.preventDefault();
    window.location.replace("/");
  });

  });