from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Team)
admin.site.register(Problems)
admin.site.register(Feedback)
admin.site.register(SolvedProblems)
