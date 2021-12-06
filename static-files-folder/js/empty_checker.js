let username = document.getElementById("username");
let password = document.getElementById("password");

function isEmptyAndWarn() {
    if (isEmpty()) {
        alert("Username or password is empty!");
        return true;
    }
    return false;
}

function isEmpty() {
    if (username.innerText.length() == 0 || password.innerText.length() == 0) {
        alert("Username or password is empty!");
        return true;
    }
    return false;
}