from django.db import models
from principal.models import Principal
from teachers.models import Teacher
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_class = models.IntegerField()
    student_age = models.CharField(max_length=20)
    principal = models.ForeignKey(Principal)
    teacher = models.ManyToManyField(Teacher)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.student_name + '---' + self.student_class
