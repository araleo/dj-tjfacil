from django.forms import ModelForm, TextInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'important', 'description']
        widgets = {
            'task': TextInput(attrs={'autofocus': 'autofocus', 'placeholder': 'Tarefa'}),
            'description': TextInput(attrs={'placeholder': 'Descrição'}),
        }
