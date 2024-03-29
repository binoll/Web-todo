function toggleTodo(id, title, complete, tag) {
	let new_completed = complete === 'True' ? 'False' : 'True';
	let newForm = new FormData();

	newForm.append("completed", new_completed);
	newForm.append("title", title);
	newForm.append("tag", tag);

	fetch(`/edit/${id}`, {
		method: "POST",
		body: newForm
	})
		.then(response => response.formData());

	setTimeout(function () {
		location.reload();
	}, 50);
}