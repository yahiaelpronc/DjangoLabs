from django.db.models import fields
from rest_framework import serializers
from .models import *

class Traineeserilzer(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        #fileds=('username','email','password','id')
        fields = '__all__'