# Generated by Django 3.2.5 on 2022-02-18 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoUsers', '0003_auto_20220218_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='user_firstname', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='lastname', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='user.jpeg', upload_to=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='short_intro',
            field=models.CharField(blank=True, max_length=230, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_link',
            field=models.URLField(default='nonew'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='username', max_length=150),
        ),
    ]
