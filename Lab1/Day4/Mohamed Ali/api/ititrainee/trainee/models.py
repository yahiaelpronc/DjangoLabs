from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)


class Trainee(models.Model):
    name=models.CharField(max_length=50)
    nationalnum = models.IntegerField(null=True)
    branch=models.IntegerField(null=True)
    courses=models.ForeignKey('Course',on_delete=models.CASCADE)