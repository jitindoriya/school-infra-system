## order of clean imports
## A good practise 


## 1. standard lib imports

## 2. core django imports

## 3. third party imports

## 4. local imports




from __future__ import unicode_literals

from django.db import models


from students.models import Student
# Create your models here.



class Attendance_student(models.Model):
	student = models.ForeignKey(Student) 