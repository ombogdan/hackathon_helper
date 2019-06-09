# Generated by Django 2.2.2 on 2019-06-09 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpapp', '0014_feedback_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolvedProblems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_problem', models.CharField(max_length=50)),
                ('program_language', models.CharField(blank=True, max_length=50)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpapp.Team')),
            ],
        ),
    ]