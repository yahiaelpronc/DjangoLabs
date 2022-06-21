from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import UpdateView
import requests
import json
# Create your views here.


def callapigetmethod(request):
    url="http://localhost:8000/trainee/listapi"
    head={'contnet-type':'application/json'}
    res=requests.get(url=url,headers=head)
    context ={'trainees': res.json()}
    return render(request,'list.html',context)



def insert(request):
    return render(request,'insert.html')

def callapiinsert(request):
    url = "http://127.0.0.1:8000/trainee/insertapi/"
    header = {
        "Content-Type": "application/json",
    }
    data = {
        "name": request.POST['name'],
        "nationalnum": request.POST['nationalnum'],
        "branch" : request.POST['branch'],
        "courses" : request.POST['courses'],
    }
    result = requests.post(url=url, data=json.dumps(data), headers=header)
    if result.status_code == 200:
        return HttpResponse('Successful Inserted')
    return HttpResponse('Something went wrong')

def edit(request,id):
    url = "http://localhost:8000/trainee/listapi"
    head = {'contnet-type': 'application/json'}
    res = requests.get(url=url, headers=head)
    trainee={}
    for t in res.json():
        if int(t['id']) == int(id):
            trainee=t

    context = {'trainee': trainee}
    return render(request,'edit.html',context)

def callapiupdate(request):
    id =request.POST['id']
    url = "http://127.0.0.1:8000/trainee/updateapi/"+id
    header = {
        "Content-Type": "application/json",
    }
    data = {
        "name": request.POST['name'],
        "nationalnum": request.POST['nationalnum'],
        "branch" : request.POST['branch'],
        "courses" : request.POST['courses'],
    }
    result = requests.put(url=url, data=json.dumps(data), headers=header)
    if result.status_code == 200:
        return HttpResponse('Successful Edit')
    return HttpResponse('Something went wrong')


def callapidelete(request):
    id=request.POST['id']
    url = "http://127.0.0.1:8000/trainee/deleteapi/"+id
    header = {
        "Content-Type": "application/json",
}
    result = requests.delete(url=url , headers=header)
    if result.status_code == 202:
        return HttpResponse('Successful Deleted')
    return HttpResponse('Something went wrong')
