$(document).ready(function() {
    $("#regBt").click(function(event) {
        event.preventDefault();
        var username = $("#username").val();
        var password = $("#password").val();
        var csrf_token = $("[name='csrfmiddlewaretoken']").val(); 

        console.log('Starting AJAX request');

        $.ajax({
            url: "/auth/",
            type: "POST",
            data: {
                username: username,
                password: password,
                csrfmiddlewaretoken: csrf_token
            },
            success: function(response) {
                if (username && password) {
                    $('#authorized').text(username);
                    console.log('success ajax');
                } else {
                    $("#errorAuth").text('Заповніть усі поля, вас не авторизовано!');
                }
            }
        });
    });
});
