from __future__ import unicode_literals

from django.db import models


from datetime import datetime


from teachers.models import Teacher
# Create your models here.
class Grade(models.Model):
	teacher = models.OneToOneField(Teacher)
	grade_name = models.CharField()              ## Need to add choices for this model ##

	def __unicode__(self):
		return self.grade_name

	def __str__unicode(self):
		return self.grade_name
		