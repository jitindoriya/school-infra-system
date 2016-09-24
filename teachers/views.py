from django.shortcuts import render, get_object_or_404
from .models import Teacher
from schoolmanagement.forms import TeacherForm,TeacherForm


# Create your views here.
def add_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        # new_teacher = form.save(commit=False)
        form.save()
        return render(request, 'teachers/teachers_details.html', {})

    context = {
        "form": form,
    }
    return render(request, 'teachers/teachers_form.html', context)


def all_teacher_details(request):
    # teacher = get_object_or_404(Teacher)
    all_teacher = Teacher.objects.all()
    return render(request, 'teachers/teachers_details.html', {'all_teacher': all_teacher})


class Add_Teacher(View):

    def get(self, request, *args, **kwargs):
        userform = UserRegistrationForm()
        teacherform = TeacherForm()

        return render(request,'teachers/addteacher.html',{'userform':userform, 'teacherform':teacherform})

    def post(self, request, *args, **kwargs):
        userform = UserRegistrationForm(request.POST)
        teacherform = TeacherForm(request.POST)

        if userform.is_valid and teacherform.is_valid:
            u = userform.save(commit=False)
            teacherform.user = u.id
            teacherform.save()
            u.save()

            return HttpResponseRedirect('/success/')
        
        return render('students/addstudent.html',{'userform':userform, 'studentform':studenform})


class LoginTeacher(View):

    def get(self, request, *args, **kwargs):
        f = TeacherLoginForm()
        return render (request, 'teachers/teacherloginform.html', {'f':f})

    def post(self, request, *args, **kwargs):
        f = TeacherLoginForm(request.POST or None)
        if f.is_valid():
            username = f.cleaned_data['username']
            password = f.cleaned_data['password']
        #@  print request.user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
        #       print request.user
         #       user = request.user
                return HttpResponseRedirect('/teacherlogin/')   
        return render (request, 'teachers/teacherloginform.html', {'f':f})

def teacherloggedin(request):
    return render('teachers/teacherprofile.html')
