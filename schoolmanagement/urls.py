from django.conf.urls import include, url
from . import views

app_name = 'schoolmanagement'

urlpatterns = [
    # Redirect to Home Page
    url(r'^$', views.index, name="index"),

]
