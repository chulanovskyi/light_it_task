function toggle(source) {
    var allChecks = $("input[name='players']");
    for(var i=0, n=allChecks.length; i<n; i++) {
        allChecks[i].checked = source.checked;
    }
}
$(function() {
    var $form = $('#create-form');
    var $checkboxes = $("input[name='players']");
    var $playersList = $("#id_players");
    var $err_message = $('<div/>', {id: 'error_message'});
    $checkboxes.change(function(){
        if ($('#error_message')){
            $playersList.css('color', '#333');
            $playersList.css('border', "0px solid red");
            $err_message.remove();
        }
    });
    $form.submit(function() {
        var checkedPlayers = $form.find('[name="players"]:checked');
        if (checkedPlayers.length < 4) {
            $err_message.text("Минимум 4 игрока");
            $playersList.before($err_message);
            $playersList.css('color', 'red');
            return false;
        }
        if (checkedPlayers.length % 2 !== 0) {
            $err_message.text("Выберите чётное количество игроков");
            $playersList.before($err_message);
            $playersList.css('color', 'red');
            return false;
        }
        return true
    });
});