from django import forms
from .models import Uroks

class UroksForm(forms.ModelForm):
    class Meta:
        model = Uroks
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введіть назву предмета (напр. Математика)'
            }),
        }