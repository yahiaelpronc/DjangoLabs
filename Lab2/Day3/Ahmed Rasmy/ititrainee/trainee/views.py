
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView

from .forms import *
from .models import Trainee,Course

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
class Updategeneric(UpdateView):
        model = Trainee
        fields = '__all__'
        success_url = "/trainee/list/"



class ViewDelete(View):


    def post(self,request):
        Trainee.objects.filter(id=request.POST['id']).delete()
        return HttpResponseRedirect("/trainee/list/")




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