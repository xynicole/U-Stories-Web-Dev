// The ID of the image that we are currently holding
// So, either accept or skip
let optionId;

// Will be useless later, just to see if everything will work
// Generates a table with mock users and stuff
function generateRandomText() {
    let randomStories = "\
        <table id='story-table'>\
            <colgroup>\
                <col span='1' style='width: 20%;'>\
                <col span='1' style='width: 80%;'>\
            </colgroup>\
            <tr>\
                <th>\
                    Title of the Story\
                </th>\
            </tr>";
    // Loops through a random number of times to create fake entries and appends them to the string
    for(i = 0; i < Math.random()*20+1; i++) {
        randomStories += "\
            <tr>\
                <td>\
                    author\
                </td>\
                <td>\
                    This is an example of a story that could potentially be submitted. it is here mostly just to test length and output. so here is some text to test that output. \
                    Wow all of these look exactly the same, that's kinda crazy, hopefully this makes sense if we have to present it like this, oh well.\
                </td>\
            </tr>";
    }
    randomStories += "</table>";
    document.getElementById("stories").innerHTML = randomStories;
}

// Kind of similar to the example code
function drop(id, evt) {
    evt.preventDefault();
    let draggedItem = document.getElementById(optionId);

    // If story is skipped, generate another story and scroll the page back to the top
    if(optionId = "skip-story") {
        generateRandomText();
        scroll(0,0);
    }   
    
    // Take story and load up another page similar to write-story.html, only without a title option
    // Keep the parent stories on page so that the user can refer to them while they are writing
    if(optionId = "accept-story") {

    }
}

// When we start to drag one of the options, update the variable to reflect that
function drag(id,evt) {
    optionId = id;
}

function allowDrop(evt) {
    evt.preventDefault();
}