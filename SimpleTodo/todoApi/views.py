from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from todo.models import Todoform


links = [
    {
        'todoList' : '/todolist/'
    },
    {
        'createTodo': '/createtodo/'
    },
    {
        'updateTodo': '/updatetodo/'
    },
    {
        'deleteTodo': '/deletetodo/'
    },
    {
        'todoDetail': '/tododetail/'
    }
]

api_view(['GET'])
def todoLinks(request):
    link = links
    return Response(link)

api_view(['GET'])
def todoList(request):
    link = Todoform.objects.all()
    serializer = TodoSerializer(link)
    return Response(serializer.data)

api_view(['GET'])
def todoDetail(request):
    link = links
    return Response(link)

api_view(['POST'])
def createTodo(request):
    link = links
    return Response(link)


api_view(['POST'])
def updateTodo(request):
    link = links
    return Response(link)

api_view(['POST'])
def deleteTodo(request):
    link = links
    return Response(link)
