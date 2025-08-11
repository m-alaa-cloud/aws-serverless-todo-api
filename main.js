const apiBaseUrl = 'https://91px294sm1.execute-api.eu-north-1.amazonaws.com/prod/tasks'; // replace if needed

// Get all tasks on load
window.onload = getTasks;

function getTasks() {
  fetch(apiBaseUrl)
    .then(res => res.json())
    .then(data => {
      const taskList = document.getElementById('taskList');
      taskList.innerHTML = '';
      data.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.taskName + " - " + task.status;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.onclick = () => deleteTask(task.TaskID);

        const editBtn = document.createElement('button');
        editBtn.textContent = 'Edit';
        editBtn.onclick = () => updateTask(task.TaskID);

        li.appendChild(deleteBtn);
        li.appendChild(editBtn);
        taskList.appendChild(li);
      });
    });
}

function createTask() {
  const taskName = document.getElementById('taskInput').value;
  const status = document.getElementById('statusSelect').value;
  const taskId = Date.now().toString();

  fetch(apiBaseUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      taskId,
      taskName,
      status
    })
  }).then(() => {
    document.getElementById('taskInput').value = '';
    getTasks();
  });
}

function updateTask(id) {
  const newName = prompt("Enter new task name:");
  const newStatus = prompt("Enter new status (Pending/Completed):");

  fetch(`${apiBaseUrl}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      taskName: newName,
      status: newStatus
    })
  }).then(() => getTasks());
}

function deleteTask(id) {
  fetch(`${apiBaseUrl}/${id}`, {
    method: 'DELETE'
  }).then(() => getTasks());
}
