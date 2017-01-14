$(document).ready(function(){
    $(".tourn-link").click(function() {
        window.location = $(this).data("href");
    });
});
/*
$('#dataTable tr td:not(:last-child)').click(function ()    {
 location.href = $(this).parent().find('td a').attr('href');
});

*/