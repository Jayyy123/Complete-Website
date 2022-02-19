from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('todoDatabase/', views.todoDatabase, name = "todoDatabase"),
    path('todoForm/', views.todoForm, name = "todoForm"),
    path('editTodoForm/<str:pk>/', views.editTodoForm, name = "editTodoForm"),
    path('deleteTodoForm/<str:pk>/', views.deleteTodoForm, name = 'deleteTodoForm')
]