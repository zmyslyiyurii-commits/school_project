from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('uroks/', views.urok_list, name='urok_list'),
    path('uroks/add/', views.urok_create, name='urok_create'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.teacher_create, name='teacher_create'),
    path('classes/', views.class_list, name='class_list'),
    path('classes/add/', views.class_create, name='class_create'),
    
    # НОВІ МАРШРУТИ ДЛЯ РОЗКЛАДУ
    path('timetable/', views.timetable_list, name='timetable_list'),
    path('timetable/add/', views.timetable_create, name='timetable_create'),
]