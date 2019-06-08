from .models import *
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email',)


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('address', 'logo')


class UserFormEdit(forms.ModelForm):
    class Meta:
        email = forms.CharField(max_length=100, required=True)
        model = User
        fields = ('username', 'email')


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        exclude = ('team',)


class AddProblemForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = ('name_problem', 'program_language')
