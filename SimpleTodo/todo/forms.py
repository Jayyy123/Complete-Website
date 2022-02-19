from .models import Todoform
from django.forms import ModelForm

class TodoForm(ModelForm):
    class Meta:
        model = Todoform
        fields = ['title','description', 'due_date']
