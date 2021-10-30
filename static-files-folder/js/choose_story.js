// The ID of the image that we are currently holding
// So, either accept or skip
let optionId;

// Kind of similar to the example code
function drop(id, evt) {
    evt.preventDefault();
    let draggedItem = document.getElementById(optionId);

    // If story is skipped, go back to story selection
    if(optionId == "skip-story") {
        window.location.href = "/p/receive-story.html";
    }   
    
    // Take story and load up another page similar to write-story.html, only without a title option
    // Keep the parent stories on page so that the user can refer to them while they are writing
    if(optionId == "accept-story") {
        
    }
}

// When we start to drag one of the options, update the variable to reflect that
function drag(id,evt) {
    optionId = id;
}

function allowDrop(evt) {
    evt.preventDefault();
}