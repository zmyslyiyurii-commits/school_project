from django import forms
from .models import Uroks, Teacher, SchoolClass, Timetable

class UroksForm(forms.ModelForm):
    class Meta:
        model = Uroks
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'urok']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'urok': forms.Select(attrs={'class': 'form-select'}),
        }

class SchoolClassForm(forms.ModelForm):
    class Meta:
        model = SchoolClass
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}

# ФОРМА РОЗКЛАДУ
class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['school_class', 'subject', 'teacher', 'day', 'lesson_number']
        widgets = {
            'school_class': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'teacher': forms.Select(attrs={'class': 'form-select'}),
            'day': forms.Select(attrs={'class': 'form-select'}),
            'lesson_number': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 8}),
        }