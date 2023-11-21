function closeAlert() {
    const alertDiv = document.querySelectorAll('.alert');
    alertDiv.forEach((div) => {
      div.addEventListener('click', (e) => {
        if (e.target.classList.contains('close-btn')) {
          div.style.display = 'none';
        }
      });
    });
  }
  document.addEventListener('DOMContentLoaded', () => {
    closeAlert();
  });