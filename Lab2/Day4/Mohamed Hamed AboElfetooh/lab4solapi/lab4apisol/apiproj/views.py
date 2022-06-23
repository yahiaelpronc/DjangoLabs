
# Create your views here.
from django.shortcuts import render
from rest_framework import status

from .models import Trainee
from .Serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def getData(req):
    person = {'name': 'mohamed', 'age': 24}
    return Response(person)
@api_view(['GET'])
def view_trainees(request,id=0):
    print(request.query_params)
    if id !=0:
        trainees = Trainee.objects.filter(id=id)
        #pass
    else:
        trainees = Trainee.objects.all()
    print(trainees)
        # if there is something in items else raise error
    if trainees:
        data = Traineeserilzer(trainees,many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def create_trainees(request):
    print(request.data)
    trainee = Traineeserilzer(data=request.data)
    # validating for already existing data
    if Trainee.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if trainee.is_valid():
        trainee.save()
        return Response(trainee.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
'''
@api_view(['POST'])
def update_trainees(request, pk):
    trainee = Trainee.objects.get(pk=pk)
    data = Traineeserilzer(instance=trainee, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

'''
@api_view(['PUT'])
def update_trainees(req,pk):
   TheChossen=Trainee.objects.get(id=pk)
   seralizer = Traineeserilzer(instance=TheChossen,data=req.data)
   if seralizer.is_valid():
       seralizer.save()
       return Response(seralizer.data)
   return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(req,id):
    trainee=Trainee.objects.get(id=id)
    trainee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

    '''
@api_view(['PUT'])
def delete(req,pk):
   TheChossen=Trainee.objects.get(id=id)
   seralizer = Traineeserilzer(instance=TheChossen,data=req.data)
   if seralizer.is_valid():
       seralizer.delete()
       return Response(seralizer.data)
   return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
