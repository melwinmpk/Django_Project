$(document).ready(function(){
    var dom = $('#taketest_div');

    var subject_ids = $(dom).attr('data-subjectIds');
    var question_Ids = $(dom).attr('data-questionids');
    console.log(typeof(question_Ids));
    console.log(question_Ids)
    console.log(JSON.parse(question_Ids.replace(/'/g, '"')))
    console.log(question_Ids['1']);
//    .attr(

});
//