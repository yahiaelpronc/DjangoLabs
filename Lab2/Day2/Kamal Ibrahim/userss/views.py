from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import registeration
# Create your views here.
def login(req):
    return render(req,'login.html')
def checklogin(req):
    checkMail=registeration.objects.filter(Email=req.POST['email'])
    checkPass=registeration.objects.filter(Password=req.POST['password'])
    if checkMail.exists() and checkPass.exists():
        return HttpResponseRedirect("/trainee/List")
def registrate(request):
    if (request.method == 'GET'):
        return render(request,'register.html')
    else :
        registeration.objects.create(Name=request.POST['name'],Email=request.POST['email'],Password=request.POST['password'])
        return HttpResponseRedirect('/userss/login')