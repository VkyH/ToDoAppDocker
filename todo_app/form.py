from django.forms import ModelForm
from .models import TodoModel

class TodoForm(ModelForm):
    class Meta:
        model=TodoModel
        fields=['task', 'status']