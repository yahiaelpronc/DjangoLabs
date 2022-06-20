from django.shortcuts import render
from .models import trainee,course
# Create your views here.
def listtrainee(req):
    outtrainne=trainee.objects.all()
    context={}
    context['title']='list of trainee'
    context['outtrainne']=outtrainne
    return render(req, 'index.html',context)
def update(req):
    courses = course.objects.all()
    outtrainne = trainee.objects.all()
    context = {}
    context['title'] = 'list of trainee'
    context['outtrainne'] = outtrainne
    INtrainne = trainee.objects.all()
    if (req.method == 'GET'):
        return render(req,'update.html',context)
    else :
        targetman=trainee.objects.get(id=req.POST['id'])
        targetman.Name=req.POST['name']
        targetman.Branch=req.POST['Branch']
        targetman.NationalNumber=req.POST['NationalID']
        targetman.Course=course.objects.get(Name=req.POST['course'])
        targetman.save()
        print(targetman)
        return render(req, 'update.html', context)
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
    context={}
    courses=course.objects.all()
    context['courses']=courses
    INtrainne = trainee.objects.all()
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
