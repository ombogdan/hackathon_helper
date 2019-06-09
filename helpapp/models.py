from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, default='Enter the floor, office and location of your team')
    logo = models.ImageField(upload_to='images/team/')

    def __str__(self):
        return str(self.user)


class Problems(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name_problem = models.CharField(max_length=50)
    program_language = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.team)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    mentor = models.CharField(max_length=50, default='Enter first and last name your mentor')
    feedback = models.CharField(max_length=500, blank=True, default='Enter your feedback')

    def __str__(self):
        return str(self.mentor)
