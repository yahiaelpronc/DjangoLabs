from django.db import models

class Course(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=True)
    '''
    def __str__(self):
        return self.name+' '+str(self.id)
    '''
class Trainee(models.Model):
    #id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    brnach=models.IntegerField(null=True)
    email=models.EmailField(max_length=50)
    #courses=models.ForeignKey(Course,on_delete=models.CASCADE,default=2)

    def __str__(self):
        return  self.name