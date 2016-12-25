/**
 * Created by oleg on 01.12.16.
 */
$(document).ready(function(){
    $(".tourn-link").click(function() {
        window.location = $(this).data("href");
    });
});
$(document).ready(function(){
    $("tr").click(function(event){
        console.log($(event.target).hasClass("remove-action"));
    });
});
/*
$('#dataTable tr td:not(:last-child)').click(function ()    {
 location.href = $(this).parent().find('td a').attr('href');
});
*/