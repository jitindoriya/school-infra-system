from django.shortcuts import render
from schoolmanagement.forms import TeacherForm
from teachers.models import Teacher


# Create your views here.
def asprincipal(request):
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
