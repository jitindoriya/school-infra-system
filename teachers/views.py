from django.shortcuts import render, get_object_or_404
from .models import Teacher
from schoolmanagement.forms import TeacherForm


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
