from django.db import models
# Create your models here.
class course(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
class trainee(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    NationalNumber = models.IntegerField(null=True)
    Branch = models.IntegerField(null=True)
    Course = models.ForeignKey('Course', on_delete=models.CASCADE)


