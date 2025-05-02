// JS
document.addEventListener('click', function(e) {
  const btn = document.querySelector('.filter-btn');
  const list = document.querySelector('.filter-list');

  if (btn.contains(e.target)) {
    // переключаем видимость списка
    list.style.display = list.style.display === 'block' ? 'none' : 'block';
  } else if (!list.contains(e.target)) {
    // клик вне кнопки и списка — скрываем
    list.style.display = 'none';
  }
});
