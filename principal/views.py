from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from schoolmanagement.forms import (TeacherForm, UserLoginForm)
from teachers.models import Teacher
from django.contrib.auth import (authenticate, login, logout, get_user_model)


# Create your views here.
def as_principal(request):
    return render(request, 'principal/principal.html', {})


def add_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        # new_teacher = form.save(commit=False)
        form.save()
        return
        # teacher_name = request.POST.get('teacher_name')
        # teacher_subject = request.POST.get('teacher_subject')
        # age = request.POST.get('teacher_age')
        # data_add_teacher = Teacher(teacher_name=teacher_name, teacher_subject=teacher_subject, teacher_age=age)
        # data_add_teacher.save()

    context = {
        "form": form,
    }
    return render(request, 'teachers/teachers_form.html', context)


def login_view(request):
    '''
    Login form for Princial as of now only
    :param request:
    :return:
    '''
    # if request.user.is_authenticated():
    #     return redirect('principal',{})

    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return render(request, 'principal/principal.html', {})
    return render(request, 'principal/login_form.html', {"form": form})


def logout_view(request):
    '''
    When User logged out redirect to homepage
    :param request:
    :return:
    '''
    logout(request)
    form = UserLoginForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'schoolmanagement/index.html', {})
