# Generated by Django 3.2.5 on 2022-02-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoform',
            name='title',
            field=models.CharField(default='empty', max_length=200),
            preserve_default=False,
        ),
    ]