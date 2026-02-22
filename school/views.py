from django.shortcuts import render, redirect
from .models import Uroks
from .forms import UroksForm

# Головна сторінка проекту
def home(request):
    return render(request, 'school/home.html')

# Сторінка зі списком предметів
def urok_list(request):
    uroks = Uroks.objects.all()
    return render(request, 'school/urok_list.html', {'uroks': uroks})

# Сторінка створення нового предмета
def urok_create(request):
    if request.method == "POST":
        form = UroksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('urok_list')
    else:
        form = UroksForm()
    return render(request, 'school/urok_form.html', {'form': form})