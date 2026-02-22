from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def home(request):
    context = {
        'teachers_count': Teacher.objects.count(),
        'classes_count': SchoolClass.objects.count(),
        'students_count': Student.objects.count(),
        'subjects_count': Uroks.objects.count(),
    }
    return render(request, 'school/home.html', context)

# Універсальна функція для списків та створення (спрощено)
def urok_list(request): return render(request, 'school/urok_list.html', {'uroks': Uroks.objects.all()})
def teacher_list(request): return render(request, 'school/teacher_list.html', {'teachers': Teacher.objects.all()})
def class_list(request): return render(request, 'school/class_list.html', {'classes': SchoolClass.objects.all()})
def student_list(request): return render(request, 'school/student_list.html', {'students': Student.objects.all()})
def timetable_list(request): return render(request, 'school/timetable_list.html', {'timetable': Timetable.objects.all()})
def grade_list(request): return render(request, 'school/grade_list.html', {'grades': Grade.objects.all()})

# Створення (приклад для нових моделей)
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'school/student_form.html', {'form': form})

def grade_create(request):
    form = GradeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('grade_list')
    return render(request, 'school/grade_form.html', {'form': form})

# Видалення (приклад)
def teacher_delete(request, pk):
    get_object_or_404(Teacher, id=pk).delete()
    return redirect('teacher_list')