from django.conf.urls import url
from .views import LoginTeacher,add_teacher,all_teacher_details, teacherloggedout,teacherloggedin

app_name = 'teachers'

urlpatterns = [
    # Redirect to Home Page
    url(r'add/$', add_teacher, name="addTeacher"),
    url(r'details/$', all_teacher_details, name="details"),
    url(r'login/$', LoginTeacher.as_view(), name='teacherlogin'),
    url(r'profile/$', teacherloggedin, name='teacherprofile'),
    url(r'^logout/', teacherloggedout, name='teacherloggedout'),

]
