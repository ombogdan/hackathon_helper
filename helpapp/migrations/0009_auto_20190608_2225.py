# Generated by Django 2.2.2 on 2019-06-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpapp', '0008_auto_20190608_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(blank=True, default='Enter your feedback', max_length=500),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='mentor',
            field=models.CharField(default='Enter first and last name your mentor', max_length=50),
        ),
    ]