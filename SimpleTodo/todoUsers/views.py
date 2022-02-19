from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UserForm,UserProfile
from .models import Profile
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


def authenticationPage(request):
    return render(request, 'todoUsers/authenticationPage.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    a = UserForm()

    if request.method == 'POST':
        a = UserForm(request.POST)
        username = request.POST['username']
        password =  request.POST['password']

        try:
            user =  User.objects.get(username = username)
        except:
            messages.error(request, 'Username or Password is incorrect')

        user = authenticate(username = username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is incorrect')
        
    return render(request, 'todoUsers/loginPage.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def signupPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    a = UserForm()
    if request.method == 'POST':
        a = UserForm(request.POST)
        if a.is_valid():
            user = a.save(commit = False)
            user.save()
            messages.success(request, 'your account has successfully been created')
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'there was an error creating your account, please try again')

        
    return render(request, 'todoUsers/signupPage.html', {'a':a})

def profile(request):
    a = Profile.objects.all()
    return render(request, 'todoUsers/profile.html',{'a':a})

def account(request,pk):
    a = Profile.objects.get(id=pk)
    return render(request, 'todoUsers/account.html',{'a':a})

def edit_profile(request, pk):
    a = Profile.objects.get(id=pk)
    b = UserProfile(instance = a)
    return render(request, 'todoUsers/profile.html',{'a':b})

