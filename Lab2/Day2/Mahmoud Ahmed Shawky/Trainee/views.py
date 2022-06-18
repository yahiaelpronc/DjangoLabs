from django.shortcuts import render
from User.models import Courses,Traine
from  django.http import HttpResponse,JsonResponse,HttpResponseRedirect


# Create your views here.
def viewinsert(request):
    context={}
    course={}
    context['main']='InsertTrainees'

    c = Courses.objects.all()
    context['courses'] = c
    return render(request,'Insert.html',context)
def Insert(request):

    Traine.objects.create(username=request.POST['username'],  national=request.POST['national'],fk_course=Courses.objects.get(Course_id=request.POST['course']))
    return render(request,'index.html')


def alltraine(request):
    t = Traine.objects.all()
    trainers = {}
    trainers['main'] = 'All Trainers'
    trainers['tr'] = t
    return render(request,'All.html',trainers)


def delete(request,list_id):
    item = Traine.objects.get(pk=list_id)
    item.delete()

    return render(request,'index.html')

def update(request,list_id):
    item = Traine.objects.get(pk=list_id)
    c2 = Courses.objects.all()
    c = Courses.objects.get(pk=item.fk_course_id)

    traineee = {}
    traineee['tr']=item
    traineee['c'] = c.Course_id
    traineee['c2'] = c2
    return render(request,'update.html',traineee)


def saveupdate(request,list_id):
    t = Traine.objects.get(id=list_id)
    t.username = request.POST['username1']
    t.national = request.POST['national1']
    t.fk_course_id=Courses.objects.get(Course_id=request.POST['course'])
    t.save()
    #member.save()


    return HttpResponseRedirect('../List')