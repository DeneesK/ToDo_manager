from django.forms import ModelForm
from .models import ToDo
from django import forms
from django.utils.translation import gettext_lazy as _


class FormTodo(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'memo', 'important']
        widgets = {
            'memo': forms.Textarea(attrs={"class": "form-control"}),
            'title': forms.TextInput(attrs={"class": "form-control"}) 
        }

