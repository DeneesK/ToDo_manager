from django.forms import ModelForm
from .models import ToDo

class FormTodo(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'memo', 'important']