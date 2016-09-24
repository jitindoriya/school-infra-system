from django import forms

from .models import Teacher

class TeacherForm(forms.ModelForm):

	class Meta:
		model = Teacher
		fields = ['teacher_age']

class TeacherLoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(widget=forms.PasswordInput)

