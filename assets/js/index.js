$(document).ready(function(){

  // jQuery methods go here...
  console.log("IS this working ????");
  alert('its working !!!!!');
  $(".login_form").find('.submit_button').unbind().bind("click",this,function(){
    var username = $(this).closest('form').find('.js_username').value();
    var password = $(this).closest('form').find('.js_password').value();
    $.ajax({
        type: "POST",
        url: '/ajax/validate_username/',
        data: {
          'mode': 'user',
          'ack': 'login',
          'username': username,
          'password':password
        },
        dataType: 'json',
        success: function (data) {
          console.log(data);
        }
    });
  });

});