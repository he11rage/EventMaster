document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.register-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const eventId = this.getAttribute('data-event-id');

      // Найти и закрыть текущую открытую модалку
      const currentModal = btn.closest('.modal');
      const bootstrapModal = bootstrap.Modal.getInstance(currentModal);
      if (bootstrapModal) {
        bootstrapModal.hide();
      }

      // Отправка AJAX-запроса на регистрацию
      fetch(`/events/register/${eventId}/`, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCSRFToken(),
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
      })
      .then(response => response.json())
      .then(data => {
        // Показать уведомление в модалке
        const modalText = document.getElementById('registrationMessageText');
        modalText.textContent = data.message;

        const messageModal = new bootstrap.Modal(document.getElementById('registrationMessageModal'));
        messageModal.show();
      })
      .catch(error => {
        console.error('Ошибка при записи:', error);
      });
    });
  });
});

// Получение CSRF-токена из куки
function getCSRFToken() {
  const cookieValue = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='));
  return cookieValue ? cookieValue.split('=')[1] : '';
}
