from django.db import models

# Create your models here.
from django.db import models
from django.db import models
# Create your models here.
class registeration(models.Model):
    Name=models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Password=models.CharField(max_length=50)