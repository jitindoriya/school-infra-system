from django.conf.urls import include, url


from .views import Add_Student

urlpatterns = [
    # Redirect to Home Page
    url(r'^addstudent/', Add_Student.as_view()),

]
