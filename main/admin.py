from django.contrib import admin
from .models import Event, Category, EventRegistration

# Регистрируем модели
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(EventRegistration)