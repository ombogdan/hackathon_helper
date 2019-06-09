from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request, 'helpapp/home.html')


def helper_sign_up(request):
    user_form = UserForm()
    team_form = TeamForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        team_form = TeamForm(request.POST, request.FILES)
        if user_form.is_valid() and team_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_team = team_form.save(commit=False)
            new_team.user = new_user
            new_team.save()
            login(request, authenticate(
                username=user_form.cleaned_data["username"],
                password=user_form.cleaned_data["password"],
            ))
            return redirect(home)
    context = {'user_form': user_form,
               'team_form': team_form}
    return render(request, 'helpapp/sign_up.html', context)


@login_required(login_url='/helper/log_in/')
def helper_account(request):
    user_form = UserFormEdit(instance=request.user)
    team_form = TeamForm(instance=request.user.team)
    if request.method == 'POST':
        user_form = UserFormEdit(request.POST, instance=request.user)
        team_form = TeamForm(request.POST, request.FILES, instance=request.user.team)
        if user_form.is_valid and team_form.is_valid:
            user_form.save()
            team_form.save()
    context = {"user_form": user_form,
               "team_form": team_form}
    return render(request, 'helpapp/account.html', context)


@login_required(login_url='/helper/log_in/')
def helper_problems(request):
    problems = Problems.objects.all()
    context = {'problems': problems}
    return render(request, 'helpapp/problems.html', context)


@login_required(login_url='/helper/log_in/')
def helper_add_problems(request):
    add_form = AddProblemForm()
    if request.method == "POST":
        add_form = ProblemForm(request.POST, request.FILES)
        if add_form.is_valid():
            add = add_form.save(commit=False)
            add.team = request.user.team
            add.save()
            return redirect(helper_problems)
    context = {'add_form': add_form}
    return render(request, 'helpapp/add_problems.html', context)


@login_required(login_url='/helper/log_in/')
def helper_edit_problems(request, id):
    problems = ProblemForm(instance=Problems.objects.get(id=id))
    if request.method == "POST":
        problems = ProblemForm(request.POST, request.FILES, instance=Problems.objects.get(id=id))
        if problems.is_valid():
            problems.save()
            return redirect(helper_problems)
    context = {'problems': problems}
    return render(request, 'helpapp/edit_problems.html', context)


@login_required(login_url='/helper/log_in/')
def helper_account_information(request, id):
    account = TeamForm(instance=Team.objects.get(id=id))
    if request.method == "POST":
        account = TeamForm(request.POST, request.FILES, instance=Team.objects.get(id=id))
        if account.is_valid():
            account.save()
            return redirect(helper_problems)
    context = {'account': account}
    return render(request, 'helpapp/edit_team.html', context)


@login_required(login_url='/helper/log_in/')
def helper_feedback(request):
    feedback = FeedbackForm()
    if request.method == "POST":
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
            return redirect(helper_feedback)
    context = {'feedback': feedback}
    return render(request, 'helpapp/feedback.html', context)


@login_required(login_url='/helper/log_in/')
def helper_delete_problems(request, id):
    if request.method == "POST":
        delete = Problems.objects.get(id=id)
        delete.delete()
        return redirect(helper_problems)
    return render(request, 'helpapp/delete_problems.html')
