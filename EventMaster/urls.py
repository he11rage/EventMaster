"""
URL configuration for EventMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main-page'),
    path('events/', views.home, name='home'),
    path('schedule/', views.schedule, name='schedule'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('get_categories/', views.get_categories, name='get_categories'),
    path('create_event/', views.create_event, name='create_event'),
    path('my-events-json/', views.user_events_json, name='user_events_json'),
    path('events/register/<int:event_id>/', views.register_for_event, name='register_for_event'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)