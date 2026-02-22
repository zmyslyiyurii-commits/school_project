from django.shortcuts import render, redirect, get_object_or_404
from .models import Uroks, Teacher, SchoolClass, Timetable
from .forms import UroksForm, TeacherForm, SchoolClassForm, TimetableForm

# Головна сторінка зі статистикою
def home(request):
    context = {
        'teachers_count': Teacher.objects.count(),
        'classes_count': SchoolClass.objects.count(),
        'subjects_count': Uroks.objects.count(),
    }
    return render(request, 'school/home.html', context)

# --- ПРЕДМЕТИ ---
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

# --- ВЧИТЕЛІ ---
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

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    teacher.delete()
    return redirect('teacher_list')

# --- КЛАСИ ---
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

# --- РОЗКЛАД ---
def timetable_list(request):
    items = Timetable.objects.all().order_by('day', 'lesson_number')
    return render(request, 'school/timetable_list.html', {'timetable': items})

def timetable_create(request):
    if request.method == "POST":
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimetableForm()
    return render(request, 'school/timetable_form.html', {'form': form})

def timetable_delete(request, pk):
    entry = get_object_or_404(Timetable, id=pk)
    entry.delete()
    return redirect('timetable_list')