from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('uroks/', views.urok_list, name='urok_list'),
    path('uroks/add/', views.urok_create, name='urok_create'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.teacher_create, name='teacher_create'),
]