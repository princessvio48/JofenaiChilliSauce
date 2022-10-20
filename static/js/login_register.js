/**redirect to home page */
var home = () => {
    window.location.href = "/";
};
/****form validation*/
// var btn_submit = document.getElementsByClassName("btn-submit");
var btn_help_text = document.getElementsByClassName("helptext");

var input = document.getElementsByTagName("input");
var password1 = "";
var password2 = "";
var username1 = "";
var email = "";
var phonenumber = "";
var taken = false;
var username_exist = [];
for (var i = 0; i < input.length; i++) {
    input[i].addEventListener("input", (e) => {
        /*register user*/
        if (e.target.name == "username1") {
            username1 = e.target.value;
            for (var i = 0; i < btn_help_text.length; i++) {
                if (i == 0) {
                    btn_help_text[i].classList.remove("hidden");
                    var input_value = e.target.value;
                    var pos = e.target.value.indexOf(" ");
                    if (pos > 0) {
                        btn_help_text[i].innerHTML = "username cannot contain whitespace";
                        btn_help_text[i].classList.remove("success");
                    } else if (input_value.length > 5) {
                        btn_help_text[i].innerHTML = "username sufficient";
                        btn_help_text[i].classList.add("success");

                        username_exist.forEach((name) => {
                            if (name == e.target.value) {
                                btn_help_text[i].innerHTML = "username already taken";
                                btn_help_text[i].classList.remove("success");
                                taken = true;
                            }
                        });
                    } else {
                        btn_help_text[i].innerHTML =
                            "username must have atleast 5 character";
                        btn_help_text[i].classList.remove("success");
                    }
                } else {
                    btn_help_text[i].classList.add("hidden");
                }
            }
        }
        /**register email */
        if (e.target.name == "email") {
            for (var i = 0; i < btn_help_text.length; i++) {
                if (i == 1) {
                    if (username1 == "") {
                        btn_help_text[i - 1].classList.remove("hidden");
                        btn_help_text[i - 1].innerHTML = "username cannot be empty";
                        e.target.value = "";
                    } else {
                        btn_help_text[i].classList.remove("hidden");
                        var input_value = e.target.value;
                        if (e.target.value.indexOf("@") > 3) {
                            btn_help_text[i].innerHTML = "email must contain . ";
                            if (e.target.value.indexOf("." > 5)) {
                                btn_help_text[i].innerHTML = "email satisfy.. ";
                                btn_help_text[i].classList.add("success");
                            } else {
                                btn_help_text[i].innerHTML = "email must contain . ";
                                btn_help_text[i].classList.remove("success");
                            }
                        } else {
                            btn_help_text[i].innerHTML = "email must contain @ and .";
                            btn_help_text[i].classList.remove("success");
                        }
                    }
                } else {
                    btn_help_text[i].classList.add("hidden");
                }
            }
            email = e.target.value;
        }

        /***register phonenumber */
        if (e.target.name == "phonenumber") {
            for (var i = 0; i < btn_help_text.length; i++) {
                if (i == 2) {
                    if (email == "") {
                        btn_help_text[i - 1].classList.remove("hidden");
                        btn_help_text[i - 1].innerHTML = "email cannot be empty";
                        e.target.value = "";
                    } else {
                        var phone = e.target.value;
                        var phoneNum = phone.replace(/[^\d]/g, "");
                        if (phoneNum.length > 6 && phoneNum.length < 11) {
                            btn_help_text[i].classList.remove("hidden");
                            btn_help_text[i].innerHTML = "phone number format satisfies";
                            btn_help_text[i].classList.add("success");
                        } else {
                            btn_help_text[i].classList.remove("hidden");
                            btn_help_text[i].innerHTML =
                                "must be a number and greater than 6";
                        }
                    }
                } else {
                    btn_help_text[i].classList.add("hidden");
                }
            }
            phonenumber = e.target.value;
        }
        /*register password */

        if (e.target.name == "password1") {
            for (var i = 0; i < btn_help_text.length; i++) {
                if (i == 3) {
                    if (phonenumber == "") {
                        btn_help_text[i - 1].classList.remove("hidden");
                        btn_help_text[i - 1].innerHTML = "phone number cannot be empty";
                        e.target.value = "";
                    } else {
                        btn_help_text[i].classList.remove("hidden");
                        var input_value = e.target.value;

                        if (input_value[0] == input_value[0].toUpperCase()) {
                            btn_help_text[i].innerHTML = "weak password";
                            btn_help_text[i].classList.remove("success");
                            if (input_value.length > 6) {
                                btn_help_text[i].innerHTML = "strong password";
                                btn_help_text[i].classList.add("success");
                            }
                        } else {
                            btn_help_text[i].classList.remove("success");
                            btn_help_text[i].innerHTML =
                                "first letter must be capital letter";
                            e.target.value = "";
                        }
                    }
                } else {
                    btn_help_text[i].classList.add("hidden");
                }
            }
            password1 = e.target.value;
        }
        /**register confirm-password */
        if (e.target.name == "password2") {
            for (var i = 0; i < btn_help_text.length; i++) {
                if (i == 4) {
                    if (password1 == "") {
                        btn_help_text[i - 1].classList.remove("hidden");
                        btn_help_text[i - 1].innerHTML = "password cannot be empty";
                        e.target.value = "";
                    } else {
                        btn_help_text[i].classList.remove("hidden");
                        password2 = e.target.value;

                        if (password1 == password2) {
                            btn_help_text[i].innerHTML = "password match";
                            btn_help_text[i].classList.add("success");
                        } else {
                            btn_help_text[i].classList.remove("success");
                            btn_help_text[i].innerHTML = "password not match";
                        }
                    }
                } else {
                    btn_help_text[i].classList.add("hidden");
                }
            }
        }
    });
}

var validation = () => {
    // var username = document.validate.username1.value;

    if (username1 == null || username1 == "") {
        btn_help_text[0].classList.remove("hidden");
        btn_help_text[0].innerHTML = "Username cannot be empty";
        return false;
    } else if (username1.length < 5) {
        btn_help_text[0].classList.remove("hidden");
        btn_help_text[0].innerHTML = "username must have atleast 5 character";

        return false;
    } else if (taken) {
        btn_help_text[0].innerHTML = "username already taken";
        btn_help_text[0].classList.remove("success");
        return false;
    } else if (password1 == null || password1 == "") {
        btn_help_text[3].classList.remove("hidden");
        btn_help_text[3].innerHTML = "password cannot be empty";
        return false;
    } else if (password1 != password2) {
        btn_help_text[4].classList.remove("hidden");
        btn_help_text[4].innerHTML = "password must match";
        return false;
    } else {
        return true;
    }
};

var username_login = document.getElementById("username");
var password_login = document.getElementById("password2");
username_login.addEventListener("input", (e) => {
    for (var i = 0; i < btn_help_text.length; i++) {
        btn_help_text[i].classList.add("hidden");
    }
});

password_login.addEventListener("input", (e) => {
    for (var i = 0; i < btn_help_text.length; i++) {
        btn_help_text[i].classList.add("hidden");
    }
});

var validation_login = () => {
    var username = document.validate.username.value;
    var password = document.validate.password2;
    if (username == null || username == "") {
        btn_help_text[1].classList.remove("hidden");
        btn_help_text[0].classList.add("hidden");
        btn_help_text[1].innerHTML = "Username cannot be empty";
        return false;
    } else if (password == null || password == "") {
        btn_help_text[2].classList.remove("hidden");
        btn_help_text[0].classList.add("hidden");
        btn_help_text[2].innerHTML = "Username cannot be empty";
        return false;
    } else {
        return true;
    }
};