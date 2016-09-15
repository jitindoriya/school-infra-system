from django.conf.urls import include, url
from . import views

app_name = 'principal'

urlpatterns = [
    # Redirect to Home Page
    url(r'^$', views.asprincipal, name="principal"),
    # url(r'teacher/add/$', views.add_teacher, name="addTeacher"),
    url(r'teacher/add/$', include('teachers.urls')),
]
