let wordCount = document.getElementById("word-count");
let inputText = document.getElementById("story-text");
let titleText = document.getElementById("title");

let pageName = document.getElementById("page-name");

let functionalWordCounter = 0;
let functionalTitleCounter = 0;
// If the word limit is being changed, don't forget to update both html files for writing and receiving stories
let MAX_SIZE = 1500;

function checkAndWarn() {
    if (isEmpty()) {
        if (pageName.value == "write") {
            alert("Either the title or body of the story is empty! You can't submit nothing!");
        }
        else {
            alert("Body of the story is empty! You can't submit nothing!");
        }
        return false;
    }
    else if (isOverLimit()) {
        alert("Body contains too many characters to be saved! Please try to shorten the story!");
        return false;        
    }    
    return true;
}
function checkWithoutWarn() {
    return (isEmpty() || isOverLimit());
}

function isEmpty() {
    if (pageName.value == "write") {
        if (functionalTitleCounter <= 0 || functionalWordCounter <= 0) {
            return true;
        }
        return false;
    }
    else {
        if (functionalWordCounter <= 0) {
            return true;
        }
        return false;
    }
}
function isOverLimit() {
    if (functionalWordCounter > MAX_SIZE) {
        return true;
    }
    return false;
}

function byteCount(s) {
    return encodeURI(s).split(/%(?:u[0-9A-F]{2})?[0-9A-F]{2}|./).length - 1;
}

// ---------- Functions for body ----------
inputText.addEventListener("keyup", (e) => wordCounter(e.target.value))

inputText.addEventListener("keydown", function(e) {
    if (functionalWordCounter >= MAX_SIZE && e.code !== "Backspace") {
        e.preventDefault();
        return;
    }
});

function wordCounter(text) {
    wordCount.innerText = byteCount(inputText.value) + (inputText.value.match(/\n/g)||[]).length;
    functionalWordCounter = byteCount(inputText.value) + (inputText.value.match(/\n/g)||[]).length;
}

// ---------- Functions for title ----------
titleText.addEventListener("keyup", (e) => titleCounter(e.target.value))

function titleCounter(text) {

    functionalTitleCounter = titleText.value.length;
}