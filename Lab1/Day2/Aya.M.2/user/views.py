from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import user

# Create your views here.

def insert(request):

    return render(request, 'Register.html')

def register(request):
    user.objects.create(Email=request.POST['email'],  lastname=request.POST['last'], password=request.POST['password'],firstname=request.POST['first'])
    return render(request, 'index.html')

def Login(request):
    log = user.objects.filter(Email=request.POST['email']) & user.objects.filter(password=request.POST['password'])

    if log.exists():
        context = {}
        context['main'] = 'Dashboard'
        return HttpResponseRedirect('../../trainee/List')
    else:
        return render(request, 'Login.html')


def login(request):

    return render(request, 'Login.html')

