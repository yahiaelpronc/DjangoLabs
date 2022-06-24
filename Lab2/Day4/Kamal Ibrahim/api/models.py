from django.db import models
from django.db import models
# Create your models here.
class Course(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=True)

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    brnach=models.IntegerField(null=True)
    def __str__(self):
        return  self.name