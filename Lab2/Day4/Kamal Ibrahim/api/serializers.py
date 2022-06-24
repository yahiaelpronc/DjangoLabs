from django.db.models import fields
from rest_framework import serializers
from .models import Trainee

class Traineeserilzer(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        fields = '__all__'