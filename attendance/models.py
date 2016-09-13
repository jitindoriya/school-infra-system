from __future__ import unicode_literals

from django.db import models


from students.models import Student
# Create your models here.



class Attendance_student(models.Model):
	student = models.ForeignKey(Student) 