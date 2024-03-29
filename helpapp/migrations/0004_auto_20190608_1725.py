# Generated by Django 2.2.2 on 2019-06-08 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpapp', '0003_auto_20190608_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problems',
            name='team',
        ),
        migrations.AddField(
            model_name='problems',
            name='team',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='helpapp.Team'),
        ),
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
        migrations.AddField(
            model_name='team',
            name='user',
            field=models.OneToOneField(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
