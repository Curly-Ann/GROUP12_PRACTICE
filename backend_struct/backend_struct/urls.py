"""
URL configuration for backend_struct project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def register_page(request):
    return render(request, 'register.html')


def login_page(request):
    return render(request, 'login.html')


def tasks_page(request):
    return render(request, 'tasks.html')


def projects_page(request):
    return render(request, 'projects.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register', register_page, name='register_page'),
    path('login', login_page, name='login_page'),
    path('tasks', tasks_page, name='tasks_page'),
    path('projects', projects_page, name='projects_page'),
    path('', include('api.urls')),
]
