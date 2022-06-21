from rest_framework import serializers
from .models import *

class Traineeser(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        # fields=['name','nationalnum','branch','courses']
        fields='__all__'