$(document).ready(function () {

    function sign_in(){
        var username = $('input[name="username"]').val();
        var password = $('input[name="password"]').val();
        $('.login_errors').hide();
        $.ajax({
            // the URL for the request
            url: "/blog/login/",

            // the data to send (will be converted to a query string)
            data: {
                username: username,
                password: password
            },

            // whether this is a POST or GET request
            type: "POST",

            // the type of data we expect back
            dataType: "json",

            // code to run if the request succeeds;
            // the response is passed to the function
            success: function (json) {
                if (json.redirect) {
                    window.location.href = json.redirect;
                }
                if (json.errors) {
                    $('.login_errors').text(json.errors).show();
                    $('input[name="username"]').val("");
                    $('input[name="password"]').val("");
                }
            },

            // code to run if the request fails; the raw request and
            // status codes are passed to the function
            error: function (xhr, status) {
                alert("Sorry, there was a problem with authentication! Please try again.");
                $('.loading-ajax').hide();
            },

            // code to run regardless of success or failure
            complete: function (xhr, status) {
                //alert( "The request is complete!" );
            }
        });
    }

    //use on sign in button to show login form
    $('.login').on('click', function () {
        $('.loginform').fadeIn("slow", "linear");
        $(this).hide();
    });


    //use on login cancel button
    $('.login_cancel').on("click", function (e) {
        //e.preventDefault();
        $('.login_errors').hide();
        $('.loginform').fadeOut(500);
        $('.login').show(1000);
    });

    // ajax request to log in
    $('#sign_in').on('click', sign_in);

    // add event when press enter on input field
    $('#id_password').on('keypress', function(event){
        if(event.which == 13){
            sign_in();
        }
    });

    //show loading bar on ajax events
    $(document).ajaxStart(function () {
        $('.loading-ajax').show();
    }).ajaxStop(function () {
            $('.loading-ajax').hide();
        }).ajaxError(function () {
            $('.loading-ajax').hide();
        });
});
