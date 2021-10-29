let wordCount = document.getElementById("word-count");
let inputText = document.getElementById("story-text");
let titleText = document.getElementById("title");

let functionalWordCounter = 0;
let functionalTitleCounter = 0;
// If the word limit is being changed, don't forget to update both html files for writing and receiving stories
let MAX_CHARACTERS = 1500;

function checkEmptyAndWarn() {
    if (isEmpty()) {
        alert("Either the title or body of the story is empty! You can't submit nothing!");
        return false;
    }
    return true;
}

function isEmpty() {
    if (functionalTitleCounter <= 0 || functionalWordCounter <= 0) {
        return true;
    }
    return false;
}

// ---------- Functions for body ----------
inputText.addEventListener("keyup", (e) => wordCounter(e.target.value))

function wordCounter(text) {
    wordCount.innerText = inputText.value.length;
    functionalWordCounter = inputText.value.length;
}

// ---------- Functions for title ----------
titleText.addEventListener("keyup", (e) => titleCounter(e.target.value))

function titleCounter(text) {

    functionalTitleCounter = titleText.value.length;
}