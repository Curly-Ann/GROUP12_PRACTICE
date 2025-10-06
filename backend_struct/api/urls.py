from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # User endpoints
    path('api/register', views.register_controller, name='register'),
    path('api/login', views.login_controller, name='login'),
    
    # Task endpoints
    path('api/tasks', views.task_controller, name='tasks'),
    path('api/tasks/<int:task_id>', views.task_detail_controller, name='task-detail'),
    
    # Project endpoints
    path('api/projects', views.project_controller, name='projects'),
]
