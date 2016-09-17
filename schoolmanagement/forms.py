from django import forms
from django.contrib.auth.models import User
from principal.models import Principal
from teachers.models import Teacher
from students.models import Student
from django.contrib.auth import (authenticate, login, logout, get_user_model)


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'teacher_subject', 'teacher_age']


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # user_queryset = User.objects.filter(username=username)
        # if user_queryset.count() == 1:
        #     user = user_queryset.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This User doesn't exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)
