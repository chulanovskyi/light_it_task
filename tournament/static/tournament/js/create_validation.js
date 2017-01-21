/**
 * Created by coal on 13.01.17.
 */
window.onload = function(){
    var form = document.getElementById('create-form');
    var checkboxes = document.querySelectorAll("input[type='checkbox']");
    var ul = document.getElementById("id_players");
    var error_message = document.createElement('div');
    error_message.setAttribute('id','error_message');

    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].onchange = function () {
            if (document.getElementById('error_message')) {
                ul.style.color = "black";
                ul.style.border = "0px solid red";
                ul.parentNode.removeChild(error_message);
            }
        }
    }
    form.onsubmit = function(){
        var n = form.querySelectorAll('[type="checkbox"]'),
            l = form.querySelectorAll('[type="checkbox"]:checked');
        for(var j=0; j< n.length; j++)
            if(l.length < 4) {
                error_message.innerHTML = "Минимум 4 игрока";
                ul.parentNode.insertBefore(error_message, ul);
                ul.style.color = "red";
                return false;
            }
            if (l.length % 2 !== 0){
                error_message.innerHTML = "Выберите чётное количество игроков";
                ul.parentNode.insertBefore(error_message, ul);
                ul.style.color = "red";
                return false;
            }
            return true
    }
};