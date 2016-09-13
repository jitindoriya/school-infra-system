## order of clean imports
## A good practise 


## 1. standard lib imports

## 2. core django imports

## 3. third party imports

## 4. local imports

from django.db import models
from django.contrib.auth.models import User



from teachers.models import Teacher
from principal.models import Principal


# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_class = models.IntegerField()
    student_age = models.CharField(max_length=20)
    principal = models.ForeignKey(Principal)
    teacher = models.ManyToManyField(Teacher)
    user = models.OneToOneField(User)
    student_pic = models.ImageField(null=True, blank=True)  ## nedd to add upload function  ##
    
    def __unicode__(self):
    	return self.student_name + '---' + self.student_class

    def __str__(self):
        return self.student_name + '---' + self.student_class
