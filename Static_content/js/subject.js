$(document).ready(function(){
  var dom = $('#subject_div');
  $(dom).find('.subject_form').find('.savesubject_button').unbind().bind('click',this,function(e){
    var subjectname = $(this).closest('.subject_form').find('.js_subjectname').val();
    e.preventDefault();
    $.ajax({
        type    : "POST",
        url     : '/ajax/request',
        dataType: 'json',
//        async: true,
        data: {
          'mode'             :'testsetup',
          'ack'              :'savesubject',
          'subjectname'      :subjectname,
          csrfmiddlewaretoken:$(dom).find(".subject_form").find('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
          if(data.status == "success")
          {
//             window.location.replace("/login");
          }
          else
          {
//            alert(data.message);
          }
        }
    });
  });

  });