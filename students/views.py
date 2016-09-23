from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from schoolmanagement.forms import UserRegistrationForm
from .forms import StudentForm

# Create your views here.
class Add_Student(View):

	def get(self, request, *args, **kwargs):
		userform = UserRegistrationForm()
		studentform = StudentForm()

		return render(request,'students/addstudent.html',{'userform':userform, 'studentform':studentform})

	def post(self, request, *args, **kwargs):
		userform = UserRegistrationForm(request.POST)
		studentform = StudentForm(request.POST)

		if userform.is_valid and studentform.is_valid:
			u = userform.save(commit=False)
			studentform.user = u.id
			studentform.save()
			u.save()

			return HttpResponseRedirect('/success/')
		
		return render('students/addstudent.html',{'userform':userform, 'studentform':studenform})
