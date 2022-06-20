from django.db import models
from django.shortcuts import render
# Create your models here.
class users(models.Model):
    id=models.AutoField(primary_key=True)
    Email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

class Courses(models.Model):
    Course_id=models.AutoField(primary_key=True)
    Cours_Name = models.CharField(max_length=100)

class Traine(models.Model):
    id=models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    national = models.CharField(max_length=50)
    fk_course = models.ForeignKey(Courses, on_delete=models.CASCADE)



