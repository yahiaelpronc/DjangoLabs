from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Trainee
from .serializers import Traineeserilzer
import requests
from django import http
# Create your views here.
@api_view(['GET'])
def getData(req):
    data=Trainee.objects.all()
    seralizer=Traineeserilzer(data,many=True)
    return Response(seralizer.data)
@api_view(['POST'])
def inserttry(req):
    print(req.data)
    seralizer=Traineeserilzer(data=req.data)
    if seralizer.is_valid():
        seralizer.save()
    return Response(seralizer.data)

@api_view(['DELETE'])
def delete(req,pk):
    TheChossen=Trainee.objects.get(id=pk)
    TheChossen.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update(req,pk):
   TheChossen=Trainee.objects.get(id=pk)
   seralizer = Traineeserilzer(instance=TheChossen,data=req.data)
   if seralizer.is_valid():
       seralizer.save()
       return Response(seralizer.data)
   return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE','POST'])
def all_views(req,pk):
    TheChossen = Trainee.objects.get(id=pk)
    if req.method == 'GET':
        data = Trainee.objects.all()
        seralizer = Traineeserilzer(data, many=True)
        return Response(seralizer.data)
    elif req.method == 'PUT':
        seralizer = Traineeserilzer(instance=TheChossen, data=req.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif req.method == 'DELETE':
        TheChossen = Trainee.objects.get(id=pk)
        TheChossen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif req.method == 'POST':
        seralizer = Traineeserilzer(data=req.data)
        if seralizer.is_valid():
            seralizer.save()
        return Response(seralizer.data)