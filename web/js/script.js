document.addEventListener('DOMContentLoaded', function () {
    showTab('addTab');
});

function showTab(tabId) {
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => {
        if (tab.id === tabId) {
            tab.style.display = 'block';
        } else {
            tab.style.display = 'none';
        }
    });
}

function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');

    if (taskInput.value.trim() !== '') {
        const taskItem = document.createElement('li');
        taskItem.textContent = taskInput.value;
        taskItem.addEventListener('click', toggleTask);

        taskList.appendChild(taskItem);
        taskInput.value = '';
    }
}

function toggleTask() {
    this.classList.toggle('completed');
}
