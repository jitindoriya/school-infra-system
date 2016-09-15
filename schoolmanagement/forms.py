from django import forms
from django.contrib.auth.models import User
from principal.models import Principal
from teachers.models import Teacher
from students.models import Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name','teacher_subject','teacher_age']
