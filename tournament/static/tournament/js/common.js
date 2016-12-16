/**
 * Created by oleg on 01.12.16.
 */
$(document).ready(function() {
        $(".tourn-link").click(function() {
            window.location = $(this).data("href");
        });
    });
