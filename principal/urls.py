from django.conf.urls import include, url
from . import views

app_name = 'principal'

urlpatterns = [
    # Redirect to Home Page
    url(r'^$', views.as_principal, name="principal"),
    # url(r'teacher/add/$', views.add_teacher, name="addTeacher"),
    url(r'teacher/add/$', include('teachers.urls')),
    url(r'login$', views.login_view, name="login"),
    url(r'logout$', views.logout_view, name="logout"),
]
