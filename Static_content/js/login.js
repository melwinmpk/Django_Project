$(document).ready(function(){

  // jQuery methods go here...

  $(".login_form").find('.submit_button').unbind().bind("click",this,function(e){
    e.preventDefault();
    var username = $(this).closest('form').find('.js_username').val();
    var password = $(this).closest('form').find('.js_password').val();
    $.ajax({
        type: "POST",
        url: '/ajax/request',
        dataType: 'json',
//        async: true,
        data: {
          'mode': 'user',
          'ack': 'login',
          'username': username,
          'password':password,
          csrfmiddlewaretoken:$(".login_form").find('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
//          alert(data);
          console.log(data);
        }
    });
  });

});