from django.conf.urls import url
from .views import LoginTeacher,add_teacher,all_teacher_details

app_name = 'teachers'

urlpatterns = [
    # Redirect to Home Page
    url(r'add/$', add_teacher, name="addTeacher"),
    url(r'details/$', all_teacher_details, name="details"),
    url(r'login/$', LoginTeacher.as_view()),
]
