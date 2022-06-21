from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from users.models import *
from .serlizer import *
import requests
# Create your views here.


@api_view(['GET'])
def view_trainees(request,id=0):
    print(request.query_params)
    if id != 0:
        trainees = Traine.objects.filter(id=id)
        #
    else:
        trainees = Traine.objects.all()
    #print(trainees)
    if trainees:
        data = trainSerializer(trainees, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_trainees(request):
    trainee = trainSerializer(data=request.data)
    if trainee.is_valid():
        trainee.save()
        return Response(trainee.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update(request, pk):
    trainee = Traine.objects.get(pk=pk)
    data = trainSerializer(instance=trainee, data=request.data)
    print(data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['delete'])
def delete(request, pk):
    trainee = Traine.objects.get(pk=pk)
    trainee.delete()

    return Response(status=status.HTTP_202_ACCEPTED)

