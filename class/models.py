from __future__ import unicode_literals

from django.db import models


from teachers.models import Teacher
# Create your models here.
class Class(models.Model):
	teacher = models.OneToOneField(Teacher)  ## give this relation a thought, i am sleepy hereafter!! ##