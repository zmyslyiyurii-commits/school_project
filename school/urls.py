from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Предмети
    path('uroks/', views.urok_list, name='urok_list'),
    path('uroks/add/', views.urok_create, name='urok_create'),
    
    # Вчителі
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.teacher_create, name='teacher_create'),
    path('teachers/delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),
    
    # Класи
    path('classes/', views.class_list, name='class_list'),
    path('classes/add/', views.class_create, name='class_create'),
    
    # Розклад
    path('timetable/', views.timetable_list, name='timetable_list'),
    path('timetable/add/', views.timetable_create, name='timetable_create'),
    path('timetable/delete/<int:pk>/', views.timetable_delete, name='timetable_delete'),
]