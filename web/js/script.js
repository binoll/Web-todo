document.getElementById("taskList").addEventListener("click", function(event) {
    var clickedElement = event.target;

    if (clickedElement.classList.contains("task") || clickedElement.classList.contains("task-completed")) {
        clickedElement.classList.toggle("task-completed");
    }
});
