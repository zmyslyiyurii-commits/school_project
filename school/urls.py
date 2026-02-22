from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('uroks/', views.urok_list, name='urok_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),
    path('classes/', views.class_list, name='class_list'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('timetable/', views.timetable_list, name='timetable_list'),
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.grade_create, name='grade_create'),
]