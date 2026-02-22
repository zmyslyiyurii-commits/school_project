from django.shortcuts import render, redirect
from .models import Uroks, Teacher, SchoolClass
from .forms import UroksForm, TeacherForm, SchoolClassForm

# Головна
def home(request):
    return render(request, 'school/home.html')

# Предмети
def urok_list(request):
    uroks = Uroks.objects.all()
    return render(request, 'school/urok_list.html', {'uroks': uroks})

def urok_create(request):
    if request.method == "POST":
        form = UroksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('urok_list')
    else:
        form = UroksForm()
    return render(request, 'school/urok_form.html', {'form': form})

# Вчителі
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'school/teacher_form.html', {'form': form})

# КЛАСИ
def class_list(request):
    classes = SchoolClass.objects.all()
    return render(request, 'school/class_list.html', {'classes': classes})

def class_create(request):
    if request.method == "POST":
        form = SchoolClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = SchoolClassForm()
    return render(request, 'school/class_form.html', {'form': form})