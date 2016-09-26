from django.conf.urls import include, url


app_name = 'students'

from .views import Add_Student, studentloggedin, LoginStudent, studentloggedout

urlpatterns = [
    # Redirect to Home Page
    url(r'^add/', Add_Student.as_view(), name='addstudent'),
    url(r'^login/', LoginStudent.as_view(), name='studentlogin'),
    url(r'^loggedin/', studentloggedin, name='studentloggedin'),
    url(r'^logout/', studentloggedout, name='studentloggedout'),

]
