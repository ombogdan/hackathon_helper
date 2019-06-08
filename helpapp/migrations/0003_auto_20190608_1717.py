# Generated by Django 2.2.2 on 2019-06-08 14:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpapp', '0002_problems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problems',
            name='team',
        ),
        migrations.AddField(
            model_name='problems',
            name='team',
            field=models.ManyToManyField(to='helpapp.Team'),
        ),
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
