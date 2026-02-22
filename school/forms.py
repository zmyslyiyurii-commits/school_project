from django import forms
from .models import Uroks, Teacher, SchoolClass, Timetable, Student, Grade

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

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'school_class']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'school_class': forms.Select(attrs={'class': 'form-select'}),
        }

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['school_class', 'subject', 'teacher', 'day', 'lesson_number']
        widgets = {f: forms.Select(attrs={'class': 'form-select'}) for f in ['school_class', 'subject', 'teacher', 'day']}
        
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'urok', 'score']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'urok': forms.Select(attrs={'class': 'form-select'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 12}),
        }