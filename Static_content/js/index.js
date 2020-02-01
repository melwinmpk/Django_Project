$(document).ready(function(){

  // jQuery methods go here...
  console.log("IS this working ????");
    alert('its working !!!!!');

    $.ajax({
        type: "POST",
        url: '/ajax/validate_username/',
        data: {
          'username': username
        },
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            alert("A user with this username already exists.");
          }
        }
      });
});