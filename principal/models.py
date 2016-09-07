from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Principal(models.Model):
    princy_name = models.CharField(max_length=100)
    princy_age = models.IntegerField()
    user = models.OneToOneField(User)

    def __str__(self):
        return self.princy_name
