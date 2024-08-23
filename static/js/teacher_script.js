  // Initialize Bootstrap modal
  var myModal = new bootstrap.Modal(document.getElementById('addTeacherModal'), {
    keyboard: false
  });

  // Toggle Edit column visibility
  document.getElementById('toggleEdit').addEventListener('click', function () {
      const editColumns = document.querySelectorAll('.edit-column');
      editColumns.forEach(column => {
          column.classList.toggle('d-none');
      });
  });

  // Toggle Delete column visibility
  document.getElementById('toggleDelete').addEventListener('click', function () {
      const deleteColumns = document.querySelectorAll('.delete-column');
      deleteColumns.forEach(column => {
          column.classList.toggle('d-none');
      });
  });