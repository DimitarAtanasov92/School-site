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

// Get the name filter input element
var nameFilter = document.getElementById("name-filter");

// Get the student list
var studentList = document.getElementsByClassName("student-list")[0];

// Add event listener to handle name filtering
nameFilter.addEventListener("input", function() {
    var filterValue = nameFilter.value.toLowerCase();
    var students = studentList.getElementsByTagName("li");

    // Loop through each student and hide/show based on the filter value
    for (var i = 0; i < students.length; i++) {
        var studentName = students[i].querySelector(".student-link").textContent.toLowerCase();
        if (studentName.includes(filterValue)) {
            students[i].style.display = "block";
        } else {
            students[i].style.display = "none";
        }
    }
});