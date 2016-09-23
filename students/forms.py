from django import forms
from django.contrib.auth.models import User

from .models import Student


class StudentForm(forms.ModelForm):

	class meta:
		model = Student
		fields = ['student_age', 'student_class']