from django.conf.urls import url
from . import views

app_name = 'principal'

urlpatterns = [
    # Redirect to Home Page
    url(r'^$', views.asprincipal, name="principal"),
]