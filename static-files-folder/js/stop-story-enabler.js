let stopper = document.getElementById("stopper");
let confirmer = document.getElementById("confirm-stop");
let author = document.getElementById("author");
let username = document.getElementById("user");

function stopAllower() {
    // console.log("Username: " + username.innerText + " Author: " + author.innerText);
    if (username.innerText == author.innerText) {
        stopper.removeAttribute("hidden");
    }
}

function unhideConfirm() {
    confirmer.removeAttribute("hidden");
}