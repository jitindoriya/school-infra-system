from __future__ import unicode_literals

from django.db import models


from teachers.models import Teacher
# Create your models here.
class Grade(models.Model):
	teacher = models.OneToOneField(Teacher)
	grade_name = models.CharField(0)

	def __unicode__(self):
		return self.grade_name

	def __str__unicode(self):
		return self.grade_name
		