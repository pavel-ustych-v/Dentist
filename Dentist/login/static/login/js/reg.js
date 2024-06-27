$(document).ready(function() {
    $("#regBt").click(function(event) {
        event.preventDefault();
        var username = $("#username").val();
        var email = $("#email").val();
        var password = $("#password").val();
        var confirm_password = $("#confirm_password").val();
        var csrf_token = $("[name='csrfmiddlewaretoken']").val();

        var special_chars = ["@", ";", ",", "!", "$", "#", "%", "^", ":", "&", ".", "*", "(", ")", "[", "]", "{", "}", "_"];
        var has_special_char = special_chars.some(char => username.includes(char));

        if (!username || !email || !password || !confirm_password) {
            $("#errorReg").text('Заповніть усі поля, вас не зареєстровано!');
            return;
        }

        if (has_special_char) {
            $("#errorReg").text('Спеціальні символи, вас не зареєстровано!');
            return;
        }

        if (!email.includes("@")) {
            $("#errorReg").text('Введіть коректну пошту, вас не зареєстровано!');
            return;
        }

        if (password !== confirm_password) {
            $("#errorReg").text('Паролі не співпадають, вас не зареєстровано!');
            return;
        }

        $.ajax({
            url: "/reg/",
            type: "POST",
            data: {
                username: username,
                email: email,
                password: password,
                confirm_password: confirm_password,
                csrfmiddlewaretoken: csrf_token
            },
            success: function(response) {
                $("#errorReg").text(response.success);
                $("#errorReg").css({'color': 'green'});
                $("#username").val('');
                $("#email").val('');
                $("#password").val('');
                $("#confirm_password").val('');
            },
            error: function(xhr) {
                var error = JSON.parse(xhr.responseText);
                $("#errorReg").text(error.error);
                $("#errorReg").css({'color': 'red'});
            }
        });
    });
});
