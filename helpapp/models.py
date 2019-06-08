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
