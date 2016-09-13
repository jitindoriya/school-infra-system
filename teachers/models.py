
## order of clean imports
## A good practise 


## 1. standard lib imports

## 2. core django imports
## 3. third party imports


from django.db import models
from django.contrib.auth.models import User


from principal.models import Principal
# Create your models here.


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    principal = models.ForeignKey(Principal)
    timestamp = models.DateTimeField(auto_now_add=True)
    user=models.OneToOneField(User)
    teacher_pic = models.ImageField(null=True, blank=True)




    def __unicode__(self):
    	return self.teacher_name + '---' + self.teacher_subject


    def __str__(self):
        return self.teacher_name + '---' + self.teacher_subject
