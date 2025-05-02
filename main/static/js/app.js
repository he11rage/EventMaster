$(document).ready(function () {
    // 🔐 Login
    $('#loginForm').submit(function (event) {
      event.preventDefault();
      const username = $('#id_username').val();
      const password = $('#id_password').val();
  
      $.ajax({
        type: 'POST',
        url: window.loginUrl,
        data: {
          username: username,
          password: password,
          csrfmiddlewaretoken: window.csrfToken
        },
        success: function (response) {
          if (response.status === 'success') {
            $('#loginModal').modal('hide');
            location.reload();
          } else {
            $('#error-message').show();
          }
        },
        error: function () {
          $('#error-message').show();
        }
      });
    });
  
    // 📝 Registration
    $('.register-button').on('click', function () {
      const login = $('#login').val();
      const name = $('#name').val();
      const surname = $('#surname').val();
      const email = $('#email').val();
      const password = $('#password').val();
  
      $.ajax({
        url: window.registerUrl,
        method: 'POST',
        data: {
          login: login,
          name: name,
          surname: surname,
          email: email,
          password: password,
          csrfmiddlewaretoken: window.csrfToken
        },
        success: function (response) {
          if (response.success) {
            alert('Регистрация прошла успешно!');
            location.reload();
          } else {
            alert('Произошла ошибка: ' + response.message);
          }
        },
        error: function () {
          alert('Произошла ошибка при отправке запроса!');
        }
      });
    });
  
    // 📂 Load categories
    $.ajax({
      url: window.getCategoriesUrl,
      method: 'GET',
      success: function (data) {
        const categorySelect = $('#category');
        data.categories.forEach(function (category) {
          categorySelect.append(new Option(category.name));
        });
      },
      error: function (error) {
        console.error("Ошибка при получении категорий:", error);
      }
    });
  
    // 📅 Create event
    $('#submitEvent').click(function () {
      const formData = new FormData();
      formData.append('title', $('#title').val());
      formData.append('description', $('#description').val());
      formData.append('city', $('#city').val());
      formData.append('place', $('#place').val());
      formData.append('start_datetime', $('#start_datetime').val());
      formData.append('end_datetime', $('#end_datetime').val());
      formData.append('category', $('#category').val());
      formData.append('price', $('#price').val());
      formData.append('capacity', $('#capacity').val());
      formData.append('image', $('#image')[0].files[0]);
      formData.append('csrfmiddlewaretoken', window.csrfToken);
  
      $.ajax({
        url: window.createEventUrl,
        method: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function (response) {
          alert('Мероприятие успешно добавлено!');
          location.reload();
        },
        error: function (error) {
          console.error("Ошибка при добавлении мероприятия:", error);
        }
      });
    });
  });
  