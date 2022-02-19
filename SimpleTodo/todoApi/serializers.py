from todo.models import Todoform
from rest_framework.serializers import ModelSerializer


class TodoSerializer(ModelSerializer):
    model = Todoform
    fields = ['title', 'description', 'due_date']