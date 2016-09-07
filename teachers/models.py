from django.db import models
from principal.models import Principal
from django.contrib.auth.models import User

# Create your models here.


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    principal = models.ForeignKey(Principal)
    teacher_subject = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    user=models.OneToOneField(User)
    def __str__(self):
        return self.teacher_name + '---' + self.teacher_subject
