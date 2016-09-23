from django.conf.urls import url
from . import views

app_name = 'teachers'

urlpatterns = [
    # Redirect to Home Page
    url(r'add/$', views.add_teacher, name="addTeacher"),
    url(r'details/$', views.all_teacher_details, name="details"),
]
