/**
 * Created by oleg on 01.12.16.
 */
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
function create_tournament() {
    var f = document.getElementById('create-form');
    var x = document.querySelectorAll("input[type='checkbox']");
    for (var i = 0; i < x.length; i++) {
        x[i].onchange = function () {
            var ul = document.querySelector("ul");
            ul.style.color = "black";
            ul.style.border = "0px solid red";
            document.getElementById("p1").innerHTML = "";
        };
    }
    f.onsubmit = function(e) {
        var n = f.querySelectorAll('[type="checkbox"]'),
            l = f.querySelectorAll('[type="checkbox"]:checked');
        for (var j = 0; j < n.length; j++) {
            if (l.length >= 4) {
                document.getElementById("p1").innerHTML = "";
                return true;
            } else {
                document.getElementById("p1").innerHTML = "Min 4 players!!!";
                var ul = document.querySelector("ul");
                ul.style.color = "red";
                return false;
            }
        }
    }
}

window.onload = create_tournament;
