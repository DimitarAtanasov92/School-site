document.addEventListener("DOMContentLoaded", function() {
    var gradeButtons = document.querySelectorAll(".grade-button");
    var flourishButtons = document.querySelectorAll(".flourish-button");
    var noteButtons = document.querySelectorAll(".note-button");

    // Add event listeners to the buttons
    gradeButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Handle the "Add Grade" button click
            console.log("Add Grade clicked");
        });
    });

    flourishButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Handle the "Add Flourish" button click
            console.log("Add Flourish clicked");
        });
    });

    noteButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Handle the "Add Note" button click
            console.log("Add Note clicked");
        });
    });
});