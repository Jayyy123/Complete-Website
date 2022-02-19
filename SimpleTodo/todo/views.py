from django.shortcuts import redirect, render
from .models import Todoform
from .forms import TodoForm


def home(request):
    
    return render(request, 'todo/home.html')

def todoForm(request):
    a = TodoForm()
    if request.method == 'POST':
        a = TodoForm(request.POST)
        if a.is_valid():
            a.save()
        return redirect('database')

    return render(request, 'todo/todoForm.html', {'a':a})

def editTodoForm(request, pk):
    a = TodoForm()
    b = Todoform.objects.get(id=pk)

    if request.method == 'POST':
        a = TodoForm(request.POST, request.FILES, instance=b)
        if a.is_valid():
            a.save()
        return redirect('database')

    return render(request, 'todo/todoForm.html')

def deleteTodoForm(request, pk):
    a = Todoform.objects.get(id=pk)
    a.delete()
    return redirect('todoDatabase')

def todoDatabase(request):
    a = Todoform.objects.all()
    return render(request, 'todo/todoDatabase.html',{'a':a})


