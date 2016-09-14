
## order of clean imports
## A good practise 


## 1. standard lib imports

## 2. core django imports
## 3. third party imports


from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from principal.models import Principal
# Create your models here.


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    principal = models.ForeignKey(Principal)
    timestamp = models.DateTimeField(auto_now_add=True)
    user=models.OneToOneField(User)
    teacher_pic = models.ImageField(null=True, blank=True)  ##Let us write a common function for this file upload ###
    slug = models.SlugField()
    
    def save(self, *args, **kwargs):
    	if not self.slug:
    		self.slug = slugify(teacher_name)
    	save(Teacher, self).save(*args, **args)	


    def get_absolute_url(self):
    	pass



    def __unicode__(self):
    	return self.teacher_name + '---' + self.teacher_subject


    def __str__(self):
        return self.teacher_name + '---' + self.teacher_subject
