from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from schoolmanagement.forms import UserRegistrationForm
from .forms import StudentForm, StudentLoginForm

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


class LoginStudent(View):

	def get(self, request, *args, **kwargs):
		f = StudentLoginForm()
		return render (request, 'student/studentloginform.html', {'f':f})

	def post(self, request, *args, **kwargs):
		f = StudentLoginForm(request.POST or None)
		if f.is_valid():
			username = f.cleaned_data['username']
			password = f.cleaned_data['password']
		#@	print request.user
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
		#		print request.user
         #       user = request.user
                return HttpResponseRedirect('/studentlogin/')	
        return render (request, 'students/studentloginform.html', {'f':f})



def studentloggedin(request):
	return render(request,'students/studentprofile.html')
