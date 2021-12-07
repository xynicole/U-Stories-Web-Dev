let stopper = document.getElementById("stopper");
let confirmer = document.getElementById("confirm-stop");
let author = document.getElementById("author");
let username = document.getElementById("user");
let hider1 = document.getElementById("hider-if-stopped1");
let hider2 = document.getElementById("hider-if-stopped2");
let deleteInit = document.getElementById("init-delete");
let confirmDelete = document.getElementById("confirm-delete");

function stopAllower() {
    // console.log("Username: " + username.innerText + " Author: " + author.innerText);
    if (username.innerText == author.innerText) {
        stopper.removeAttribute("hidden");
        deleteInit.removeAttribute("hidden");
    }
}

function unhideConfirmStop() {
    confirmer.removeAttribute("hidden");
}

function unhideConfirmDelete() {
    confirmDelete.removeAttribute("hidden");
}

function hider() {
    hider1.style.display = "none";
    hider2.style.display = "none";
}