from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import registeration
from .forms import *
# Create your views here.
def login(req):
        return render(req,'login.html')

def checklogin(req):

        checkU=registeration.objects.filter(
            Name=req.POST['name'],
            Password=req.POST['password'])
        print("noppppe",checkU,req.POST['name'])
        authenticateUser=authenticate(
            username=req.POST['name'],
            password=req.POST['password'])
        print("lollllll", authenticateUser)
        if (len(checkU)!=0 and authenticateUser is not None):
            req.session['loginid'] = checkU[0].id
            return HttpResponseRedirect("/trainee/List")
        else:
            return render(req,'login.html',{'error': 'invalid credentails'})

def registrate(request):
    fom=RegisterForm()
    context={}
    context['form']=fom
    if (request.method == 'GET'):
        return render(request,'register.html',context)
    else :
        us=registeration()
        us.Name=request.POST['Name']
        us.Email=request.POST['Email']
        us.Password=request.POST['Password']
        us.save()
        User.objects.create_user(username=request.POST['Name'],
            email=request.POST['Email'],
            password=request.POST['Password'], is_staff=True)
        return HttpResponseRedirect('/login')

def userLogout(request):
    logout(request)
    return HttpResponseRedirect("/login")