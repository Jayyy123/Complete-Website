from mimetypes import init
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver


@receiver(post_save, sender = User)
def CreateProfile(created,instance, sender ,**kwargs):
    print('values')
    if created:
        user = instance
        profile = Profile.objects.create(
            owner = user,
            first_name = user.first_name,
            last_name  = user.last_name,
            username = user.username

        )