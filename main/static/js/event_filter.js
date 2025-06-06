document.addEventListener('DOMContentLoaded', function () {
  const checkboxes = document.querySelectorAll('.category-checkbox');
  const eventCards = document.querySelectorAll('.event-card');

  function updateVisibility() {
    const selected = Array.from(checkboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.value);

    eventCards.forEach(card => {
      const cardCategory = card.dataset.category;

      if (selected.length === 0 || selected.includes(cardCategory)) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  }

  checkboxes.forEach(cb => cb.addEventListener('change', updateVisibility));
});
