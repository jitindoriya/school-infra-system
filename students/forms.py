from django import forms
from django.contrib.auth.models import User

from .models import Student


class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ['student_age', 'student_class']


class StudentLoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(widget=forms.PasswordInput)
	
