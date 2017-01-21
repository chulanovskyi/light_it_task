/**
 * Created by oleg on 20.01.17.
 */
// Change Edit button to Save button + add inputs to form
var selector = '';
var score = '';
// Add inputs and button save for form
$("button.edit").click(function () {
    var id = $(this).attr("id");
    selector = "#id" + id;
    score = 'div' + selector + ' ';
    $(score + '.score-first').html('<input name="team_1_score" type="number" min="0" required>');
    $(score + '.score-second').html('<input name="team_2_score" type="number" min="0" required>');
    $(score + 'button.save').attr("style", "display:block");
    $(score + 'button.edit').attr("style", "display:none");
});


// Submit post on submit
var form = 'form' + selector;
$(form).on('submit', function (event) {
    event.preventDefault();
    console.log("form submitted!");  // sanity check
    var match_id = $(this).attr("class");
    console.log(match_id);
    create_post(match_id);
});

// AJAX for posting
function create_post(match_id) {
    console.log("create post is working!") // sanity check
    $.ajax({
        url: "match_score/", // the endpoint
        type: "POST", // http method
        data: {
            team_1_score: $('.score-first input').val(),
            team_2_score: $('.score-second input').val(),
            match_id: match_id
        }, // data sent with the post request

        // handle a successful response
        success: function (json) {
            $(score + '.score-first input').attr("disabled", "");
            $(score + '.score-second input').attr("disabled", "");
            $(score + 'button.save').attr("disabled", "");
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


$(function () {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    /*
     The functions below will create a header with csrftoken
     */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});