$(document).ready(function() {
    $("#regBt").click(function(event) {
        event.preventDefault();
        var username = $("#username").val();
        var email = $("#email").val();
        var password = $("#password").val();
        var confirm_password = $("#confirm_password").val();
        var csrf_token = $("[name='csrfmiddlewaretoken']").val(); 

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
            success: function() {
                if (username && password && email && confirm_password) {
                    if (! email.includes("@", ";", ',', '!', '$', '#', ' %', '^', ':', '&', '.', '*', '(', ')', '[', ']', '{', '}')){
                        if (email.includes("@")){
                             if (password == confirm_password){
                                 $("#errorReg").text('Вас успішно зареєстровано!');
                                 $("#errorReg").css({'color':'red'})
                                 $("#username").text('');
                                 $("#email").text('');
                                 $("#password").text('');
                                 $("#confirm_password").text('');   
                                 }else {
                                     $("#errorReg").text('Паролі не співпадають, вас не зареєстровано!');
                                 }            
                             }else {
                                 $("#errorReg").text('Введіть коректну пошту, вас не зареєстровано!');
                             }   
                         }else {
                            $("#errorReg").text('Спеціальні символи, вас не зареєстровано!');
                         }
                    }else {
                        $("#errorReg").text('Заповніть усі поля, вас не зареєстровано!');
                    } 
                          
                }
})
})
})
