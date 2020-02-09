  $(document).ready(function(){
      var dom = $('#questionAdd_div');
      $(dom).find('#selectquestionType').on('change',this, function(e) {
        var id  = $(this).val();
        $(dom).find('.tab-content').find('.tab-pane').removeClass('active in')
        $(dom).find('.tab-content').find('.tab-pane'+'.'+id).addClass("active in");
      });
      $(dom).find('.js_moreoptions').unbind().bind('click',this,function(){
        var count = $(dom).find('.mcqoptions .optiondiv').length +1;
        var optiondiv_html = '<div class="optiondiv">'+
                                '<span>Option '+count+':</span>'+
                                '<input class="js_option" type="text" placeholder="option '+count+'">'+
                                '<button class="js_canceloption">Cancel</button>'+
                             '</div>';
        $(dom).find('.mcqoptions').append(optiondiv_html);
        $(dom).find('.js_canceloption').unbind().bind('click',this,function(){
            $(this).closest('.optiondiv').remove();
        });
      });
//      selectSubject js_moreoptions
  });
