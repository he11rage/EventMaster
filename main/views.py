from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import Event, Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Event
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Event, EventRegistration
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST


def main(request):
    return render(request, "main/main-page.html")

def home(request):
    events = Event.objects.all()
    categories = Category.objects.all()
    return render(request, "main/index.html", {
        'events': events,
        'categories': categories,
    })


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


# Получаем все категории
def get_categories(request):
    categories = Category.objects.all()
    category_data = [{'name': category.name} for category in categories]
    return JsonResponse({'categories': category_data})

# Создание мероприятия через AJAX
@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
            city = request.POST.get('city')
            place = request.POST.get('place')
            start_datetime = request.POST.get('start_datetime')
            end_datetime = request.POST.get('end_datetime')
            category_name = request.POST.get('category')
            price = request.POST.get('price')
            capacity = request.POST.get('capacity')
            image = request.FILES.get('image')

            # Валидация на пустые поля или неправильные данные
            if not title or not description or not city:
                return JsonResponse({'error': 'Недостаточно данных для создания события'}, status=400)

            # Получаем объект категории по имени
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                return JsonResponse({'error': f'Категория "{category_name}" не найдена'}, status=400)

            organizer = request.user

            # Сохраняем событие в базе данных
            # Например, если используешь модель Event:
            event = Event.objects.create(
                title=title,
                description=description,
                city=city,
                place=place,
                start_datetime=start_datetime,
                end_datetime=end_datetime,
                category=category,
                price=price,
                capacity=capacity,
                image=image,
                organizer=organizer,
            )

            return JsonResponse({'message': 'Мероприятие успешно добавлено!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Неверный метод запроса'}, status=400)


def schedule(request):
    return render(request, "main/schedule.html")

@login_required
def user_events_json(request):
    registrations = EventRegistration.objects.filter(user=request.user).select_related('event')
    data = [
        {
            'title': reg.event.title,
            'start': reg.event.start_datetime.isoformat(),
            'end': reg.event.end_datetime.isoformat() if reg.event.end_datetime else None,
        }
        for reg in registrations
    ]
    return JsonResponse(data, safe=False)

@login_required
@require_POST
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    already_registered = EventRegistration.objects.filter(user=request.user, event=event).exists()
    if already_registered:
        return JsonResponse({'success': False, 'message': 'Вы уже записались на это мероприятие.'})

    EventRegistration.objects.create(user=request.user, event=event)
    return JsonResponse({'success': True, 'message': 'Вы успешно записались!'})