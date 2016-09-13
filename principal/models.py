
## order of clean imports
## A good practise 


## 1. standard lib imports

## 2. core django imports
## 3. third party imports

## 4. local imports


from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Principal(models.Model):
    princy_name = models.CharField(max_length=100)
    princy_age = models.IntegerField()
    user = models.OneToOneField(User)
    princy_pic = models.ImageField(null=True, blank=True)

    def __unicode__(self):
    	return self.princy_name

    def __str__(self):
        return self.princy_name
