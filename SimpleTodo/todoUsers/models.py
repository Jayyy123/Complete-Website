from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=False, null = False, default = "user_firstname")
    last_name = models.CharField(max_length=150, blank=False, null = False,default = "lastname")
    username = models.CharField(max_length=150, blank=False, null = False,default = "username")
    profile_picture = models.ImageField( default = 'user.jpeg')
    short_intro =  models.CharField(max_length = 230, blank=True, null=True)
    social_link = models.URLField(default='nonew')
    bio =  models.TextField(blank=True, null=True)
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)

    def __str__(self) -> str:
        return self.username