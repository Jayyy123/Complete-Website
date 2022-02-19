from operator import mod
from .models import Profile
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password1', 'password2']

class UserProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'username','bio', 'profile_picture', 'short_intro', 'social_link']