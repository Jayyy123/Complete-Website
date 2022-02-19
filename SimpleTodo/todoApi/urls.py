from django.urls import path
from . import views


urlpatterns = [
    path('', views.todoLinks, name = 'links'),
    path('todolist/', views.todoList, name = 'list'),
    path('createtodo/', views.createTodo, name = 'createtodo'),
    path('tododetail/', views.todoDetail, name = 'tododetail'),
    path('updatetodo/<str:pk>/', views.updateTodo, name = 'updatetodo'),
    path('deletetodo/<str:pk>/', views.deleteTodo, name = 'deletetodo'),
]