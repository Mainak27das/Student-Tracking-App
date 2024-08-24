
document.getElementById('toggleEdit').addEventListener('click', function () {
	document.querySelectorAll('.edit-column').forEach(column => column.classList.toggle('d-none'));
});

document.getElementById('toggleDelete').addEventListener('click', function () {
	document.querySelectorAll('.delete-column').forEach(column => column.classList.toggle('d-none'));
});

