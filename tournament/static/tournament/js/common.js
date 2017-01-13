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

/* For Create-tournament FORM */
$(document).ready(function(){
  $('.modal-body form').submit(function(){
    var x = 0;
    $('li label input').each(function(){
      if ($(this).prop('checked')) {
        x += 1
     }
    });
    if (x<4) {
      alert('You must choose 4 players at least');
      return false
    }
    else if (x%2 !== 0) {
      alert('Сhoose only an even number of players');
      return false
    }
    return true
  })
});