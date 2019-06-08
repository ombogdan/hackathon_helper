# Generated by Django 2.2.2 on 2019-06-08 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpapp', '0004_auto_20190608_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpapp.Team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
