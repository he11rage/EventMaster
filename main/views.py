from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User


def home(request):
    return render(request, "main/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse(
                {"status": "error"}, status=400
            )  # возвращаем ошибку при неправильных данных

    return render(request, "main/index.html")

def register_view(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if login and name and surname and email and password:
            try:
                user = User.objects.create_user(username=login, email=email, password=password, first_name=name,
                                                last_name=surname)
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        else:
            return JsonResponse({'success': False, 'message': 'Не все поля заполнены'})
    