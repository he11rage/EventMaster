from django.contrib import admin
from .models import Event, Category

# Регистрируем модели
admin.site.register(Event)
admin.site.register(Category)
