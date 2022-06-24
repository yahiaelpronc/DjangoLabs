from django.shortcuts import render
from .models import trainee,course
from userss.models import registeration
from .forms import *
from django.http import HttpResponseRedirect
from .models import *
#Hint 
#sorry i make the form in update not list 
#def update2 this one with form 
# Create your views here.
def listtrainee(req):
    if ('loginid' not in req.session):
        outtrainne = trainee.objects.all()
        context = {}
        context['title'] = 'list of trainee'
        context['outtrainne'] = outtrainne
        if ('loginid' in req.session):
            loggeduser =registeration.objects.get(id=req.session['loginid'])
            context['username'] = loggeduser.Name
            print(loggeduser.Name)
            return render(req, 'index.html', context)
        return render(req, 'index.html',context)
    else :
        return HttpResponseRedirect("/login")
def update(req):
    if ('loginid' not in req.session):
        context={}
        courses = course.objects.all()
        outtrainne = trainee.objects.all()
        context['title'] = 'list of trainee'
        context['outtrainne'] = outtrainne
        INtrainne = trainee.objects.all()
        if (req.method == 'GET'):
            return render(req,'update.html',context)
        else :
            return render(req, 'update2.html', context)
    else :
        return HttpResponseRedirect("/login")
def update2(req,id1):
    if ('loginid' not in req.session):
        context = {}
        print(id1)
        fom = updateForm()
        context['form'] = fom
        context['id']=id1
        if (req.method == 'GET'):
            return render(req, 'update2.html', context)
        else:
            targetman = trainee.objects.get(id=id1)
            targetman.Name = req.POST['Name']
            targetman.Branch = req.POST['Branch']
            targetman.NationalNumber = req.POST['NationalNumber']
            targetman.Course = course.objects.get(Name=req.POST['Course'])
            targetman.save()
            print(targetman)
            return HttpResponseRedirect("/trainee/update")
    else :
        return HttpResponseRedirect("/login")
from django.views import View
class Delete(View):

        context = {}
        outtrainne = trainee.objects.all()
        context['title'] = 'delete of trainee'
        context['outtrainne'] = outtrainne
        def get(self,request):
            context = {}
            outtrainne = trainee.objects.all()
            context['title'] = 'delete of trainee'
            context['outtrainne'] = outtrainne
            return render(request, 'delete.html', context)
        def post(self,request):
            context = {}
            outtrainne = trainee.objects.all()
            context['title'] = 'delete of trainee'
            context['outtrainne'] = outtrainne
            idl = request.POST['id']
            trainee.objects.filter(id=idl).delete()
            return render(request, 'delete.html', context)

def delete(req):
    context={}
    outtrainne = trainee.objects.all()
    context['title'] = 'delete of trainee'
    context['outtrainne'] = outtrainne
    if (req.method == 'GET'):
        return render(req, 'delete.html', context)
    else :
        idl=req.POST['id']
        trainee.objects.filter(id=idl).delete()
        return render(req, 'delete.html', context)

def insert(req):
    outtrainne = trainee.objects.all()
    context={}
    courses=course.objects.all()
    context['courses']=courses
    INtrainne = trainee.objects.all()
    context['outtrainne'] = outtrainne
    context['title'] = 'insert into trainees'
    if (req.method == 'GET'):
        return render(req, 'insert.html', context)
    else:
        trainee.objects.create(
            id=req.POST['id'],
            Name=req.POST['name'],
            Branch=req.POST['Branch'],
            NationalNumber=req.POST['NationalID'],
            Course=course.objects.get(id=req.POST['course']))
        return render(req,'insert.html',context)
from django.views.generic.edit import UpdateView
class updategrn(UpdateView):
    model = trainee
    fields =[
        "id","Name","Branch","NationalNumber","Course"
    ]
    success_url="/trainee/List"
