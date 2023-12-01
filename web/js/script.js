function toggleTask(taskId) {
    const taskElement = document.querySelector(`.task${taskId}`);

    if (taskElement.classList.contains('task-complete')) {
        // Make a POST request to "/edit/{{ task.id }}"
        const url = `/edit/${taskId}`;
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // Add any additional headers if needed
            },
            // Add any additional data you want to send in the body
            body: JSON.stringify({}),
        })
        .then(response => {
            // Handle the response as needed
            console.log('POST request successful');
        })
        .catch(error => {
            // Handle errors
            console.error('Error making POST request:', error);
        });
    }

    // Add or remove the "task-complete" class based on the current state
    taskElement.classList.toggle('task-complete');
}