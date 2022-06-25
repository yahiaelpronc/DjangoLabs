
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import UpdateView

from .forms import *
from .models import Trainee,Course
from django.shortcuts import render
from rest_framework.response import Response
from . models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def listApi(request,id=0):
    if(id==0):
        trainess=Trainee.objects.all()
        if(trainess is not None):
            data=Traineeser(trainess,many=True)
        return  Response(data.data)
    else:
        trainee=Trainee.objects.filter(id=id)[0]
        if(trainee):
            data=Traineeser(trainee)
            return Response(data.data)
        else:
            return Response({'error':'trainee not found'})

@api_view(['POST'])
def insertApi(request):

    trainee=Traineeser(data=request.data)
    if(trainee.is_valid()):
        trainee.save()
        return Response(trainee.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateApi(request,pk):
    traineechk = Trainee.objects.get(id=pk)
    data=Traineeser(instance=traineechk,data=request.data)

    if (data.is_valid()):
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def deleteApi(request,pk):
    trainee = get_object_or_404(Trainee, id=pk)
    trainee.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


























def list(request):
    trainees=Trainee.objects.all()
    context={}
    context['title']='List Student In Iti'
    context['trainees']=trainees
    return render(request,'list.html',context)
def insert(request):
    context={}
    courses = Course.objects.all()
    context['courses'] = courses
    finsert = InsertForm()
    context['form'] = finsert
    if(request.method=='GET'):
        return render(request,'insert.html',context)
    else:
            finsert = InsertForm( request.POST )
            if(finsert.is_valid()):

                Trainee.objects.create(name=request.POST['name'], nationalnum=request.POST['nationalnum'], courses = Course.objects.get(id=request.POST['courses']), branch=request.POST['branch'])
                return HttpResponseRedirect('/trainee/list/')
            else:
                context['errors'] = finsert.errors
                return render(request, 'insert.html', context)




def update(request,id):

    trainee=Trainee.objects.get(id=id)
    context = {}
    context['title'] = 'Update Trainee'
    context['trainee'] = trainee
    courses = Course.objects.all()
    context['courses'] = courses
    return render(request, 'update.html', context)
def updatetrainee(request,id):
    Trainee.objects.filter(id=id).update(name=request.POST['name'],nationalnum=request.POST['nationalnum'],courses=Course.objects.get(id=request.POST['course']),branch=request.POST['branch'])
    return HttpResponseRedirect("/trainee/list/")


def delete(request,id):
    Trainee.objects.filter(id=id).delete()
    return HttpResponseRedirect("/trainee/list/")

class Updategeneric(UpdateView):
        model = Trainee
        fields = '__all__'
        success_url = "/trainee/list/"


class ViewDelete(View):

    def post(self, request):
        Trainee.objects.filter(id=request.POST['id']).delete()
        return HttpResponseRedirect("/trainee/list/")
