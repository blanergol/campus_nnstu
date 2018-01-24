// csrf
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
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

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

$(document).ready(function () {
    // подсвечиваем активный пункт меню
    $("#header_havigation li a").each(function () {
        var location = window.location.href;
        var link = this.href;
        if (location === link) {
            $(this).parent("li").addClass("active");
        }
    });

    // авторизация пользователя
    $("#auth-form").submit(function () {
        $.ajax({
            type: $("#auth-form").attr("method"),
            url: $("#auth-form").attr("action"),
            data: $("#auth-form").serialize(),
            success: function (data) {
                data = JSON.parse(data);
                if (data.status === "success") {
                    window.location.href = data.redirect;
                } else if (data.status === "fail") {
                    $("#auth-form-message").removeClass("text-success");
                    $("#auth-form-message").addClass("text-danger");
                    $("#auth-form-message").html('Пользователь не найлен, email или пароль не верны.');
                }
            },
            error: function (data) {
                $("#auth-form-message").removeClass("text-success");
                $("#auth-form-message").addClass("text-danger");
                $("#auth-form-message").html("Данные не отправлены, ошибка сервера. Попробуйте еще раз.");
            }
        });
        return false;
    });

    // регистрация пользователя
    $("#reg-form").submit(function () {
        $.ajax({
            type: $("#reg-form").attr("method"),
            url: $("#reg-form").attr("action"),
            data: $("#reg-form").serialize(),
            success: function (data) {
                data = JSON.parse(data);
                if (data.status === "success") {
                    window.location.href = data.redirect;
                } else if (data.status === "fail") {
                    $("#reg-form-message").removeClass("text-success");
                    $("#reg-form-message").addClass("text-danger");
                    $("#reg-form-message").html('');
                }
            },
            error: function (data) {
                $("#reg-form-message").removeClass("text-success");
                $("#reg-form-message").addClass("text-danger");
                $("#reg-form-message").html("Данные не отправлены, ошибка сервера. Попробуйте еще раз.");
            }
        });
        return false;
    });

    // регистрация пользователя с главной страницы
    // backend добавляет в куки данные
    // редиректит на страницу заполнения полных данных
    $("#reg-mp-form").submit(function () {
        $.ajax({
            type: $("#reg-mp-form").attr("method"),
            url: $("#reg-mp-form").attr("action"),
            data: $("#reg-mp-form").serialize(),
            success: function (data) {
                data = JSON.parse(data);
                window.location.href = data.redirect;
            },
            error: function (data) {
                $("#reg-mp-form-message").removeClass("text-success");
                $("#reg-mp-form-message").addClass("text-danger");
                $("#reg-mp-form-message").html("Данные не отправлены, ошибка сервера. Попробуйте еще раз.");
            }
        });
        return false;
    });

    // отправка вопроса из виртуальной приемной
    $("#issues-form").submit(function () {
        $.ajax({
            type: $("#issues-form").attr("method"),
            url: $("#issues-form").attr("action"),
            data: $("#issues-form").serialize(),
            success: function (data) {
                data = JSON.parse(data);
                if (data.status === "success") {
                    $("#issues-form-message").removeClass("text-danger");
                    $("#issues-form-message").addClass("text-success");
                    $("#issues-form-message").html('Спасибо за обращение. Ваш вопрос отправлен. Вы получите ответ в ближайшее время.');
                } else if (data.status === "fail") {
                    $("#issues-form-message").addClass("text-danger");
                    $("#issues-form-message").removeClass("text-success");
                    $("#issues-form-message").html('Ваш вопрос не был отправлен. Ошибка сервера. Попробуйте еще раз.');
                }
            },
            error: function (data) {
                $("#issues-form-message").removeClass("text-success");
                $("#issues-form-message").addClass("text-danger");
                $("#issues-form-message").html("Данные не отправлены, ошибка сервера. Попробуйте еще раз.");
            }
        });
        return false;
    });
});