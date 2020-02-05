$(document).ready(function(){
  var dom = $('#register_div');
  $(dom).find('.register_form .submit_button').unbind().bind("click",this,function(e){
    e.preventDefault();
    var username   = $(this).closest('form').find('.js_username').val();
    var password   = $(this).closest('form').find('.js_password').val();
    var first_name = $(this).closest('form').find('.js_first_name').val();
    var last_name  = $(this).closest('form').find('.js_last_name').val();
    var email      = $(this).closest('form').find('.js_email').val();
    var password2  = $(this).closest('form').find('.js_password2').val();

    if(!(password === password2))
    {
        alert("Password Doesnot Match !");
        return
    }
    $.ajax({
        type    : "POST",
        url     : '/ajax/request',
        dataType: 'json',
//        async: true,
        data: {
          'mode'             :'user',
          'ack'              :'register',
          'username'         :username,
          'password'         :password,
          'first_name'       :first_name,
          'last_name'        :last_name,
          'email'            :email,
          csrfmiddlewaretoken:$(dom).find(".register_form").find('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
//          alert(data);
          console.log(data);
        }
    });
  });

});