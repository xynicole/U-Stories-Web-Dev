let wordCount = document.getElementById("word-count");
let inputText = document.getElementById("story-text");
let titleText = document.getElementById("title");

let functionalWordCounter = 0;
let functionalTitleCounter = 0;
// If the word limit is being changed, don't forget to update both html files for writing and receiving stories
let MAX_WORDS_FOR_BODY = 500;
let MAX_WORDS_FOR_TITLE = 30;

// I don't think this actually does anything lol
function setWordCounter() {
    if (inputText.value.split('').length != 0) {
        wordCounter(inputText.innerText);
    }
}

// ---------- WARNINGS ----------
function checkWordLimitAndWarn() {
    if (!checkWordLimit()) {
        alert('Too many words in the story or title! Please keep in mind the word limit!\nWord limit for the title is ' + MAX_WORDS_FOR_TITLE + "!");
        return false;
    }
    return true;
}

function checkWordLimit() {
    if (functionalWordCounter > MAX_WORDS_FOR_BODY-1 || functionalTitleCounter > MAX_WORDS_FOR_TITLE-1) {
        return false;
    }
    return true;
}

// ---------- Functions for body ----------
inputText.addEventListener("keyup", function(e){
    wordCounter(e.target.value);
});

inputText.addEventListener("keydown", function(e) {
    if (functionalWordCounter > MAX_WORDS_FOR_BODY-1 && e.code !== "Backspace") {
        e.preventDefault();
        return;
    }
});

function wordCounter(text) {
    var text = inputText.value.split(' ');
    var words = 0;
    for (var i = 0; i < text.length; i++) {
        if (text[i] !== ' ' && isWord(text[i])) {
            words++;
        }
    }
    wordCount.innerText = words;
    functionalWordCounter = words;
}

// ---------- Functions for title ----------
titleText.addEventListener("keyup", function(e){
    titleCounter(e.target.value);
});

titleText.addEventListener("keydown", function(e) {
    if (functionalTitleCounter > MAX_WORDS_FOR_TITLE-1 && e.code !== "Backspace") {
        e.preventDefault();
        return;
    }
});

function titleCounter(text) {
    var text = titleText.value.split(' ');
    var words = 0;
    for (var i = 0; i < text.length; i++) {
        if (text[i] !== ' ' && isWord(text[i])) {
            words++;
        }
    }
    functionalTitleCounter = words;
}

// ---------- Shared function for title and body ----------
function isWord(str) {
    let alphaNumericFound = false;
    for (let i = 0; i < str.length; i++) {
        let code = str.charCodeAt(i);
        if ((code > 47 && code < 58) || // numeric (0-9)
            (code > 64 && code < 91) || // upper alpha (A-Z)
            (code > 96 && code < 123)) { // lower alpha (a-z)
            alphaNumericFound = true;
            return alphaNumericFound;
        }
    }
    return alphaNumericFound;
}