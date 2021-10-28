
let optionId;

// Will be useless later, just to see if everything will work
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
    for(i = 0; i < Math.random()*20+1; i++) {
        randomStories += "\
            <tr>\
                <td>\
                    author\
                </td>\
                <td>\
                    this is an example of a story that could potentially be submitted. it is here mostly just to test length and output. so here is some text to test that output. \
                    Wow all of these look exactly the same, that's kinda crazy, hopefully this makes sense during the presentation, oh well.\
                </td>\
            </tr>";
    }
    randomStories += "</table>";
    document.getElementById("stories").innerHTML = randomStories;
}

function drop(id, evt) {
    evt.preventDefault();
    let draggedItem = document.getElementById(optionId);

    //id.innerHTML = draggedItem.innerHTML;

    if(optionId = "skip-story") {
        generateRandomText();
    }   
    
    if(optionId = "accept-story") {

    }
}

function drag(id,evt) {
    optionId = id;
}

// this will be called when we drag into our fence
function allowDrop(evt) {
    evt.preventDefault();
}