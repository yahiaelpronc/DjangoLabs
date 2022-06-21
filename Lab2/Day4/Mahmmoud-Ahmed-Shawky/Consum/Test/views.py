from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
from rest_framework import status
from  django.http import HttpResponse,HttpResponseRedirect
import requests
from Test import *
import json
from django.http import HttpResponse
# Create your views here.
def getTest(request):
    url = "http://127.0.0.1:8000/API/get/"
    header = {
        "Content-Type": "application/json",
    }

    result = requests.get(url=url, headers=header)
    print(result.json())

    if result.status_code == 200:
        context={}
        context['trainees']=result.json()

    return render(request, 'index.Html', context)


def postTest(request):

    if request.method=='GET':
        return  render(request,'post.html')
    else:

                url = "http://127.0.0.1:8000/API/insert/"
                header = {
                    "Content-Type": "application/json",

                }

                data={
                    "id": request.POST['id'],
                    "username": request.POST['username'],
                    "national": request.POST['national'],
                    "fk_course": 1
                }
                result = requests.post(url=url,data=json.dumps(data), headers=header)
                print(result.json())
                if result.status_code == 200:
                    return HttpResponse('Successful')
                return HttpResponse('Something went wrong')

def updateTestv(request):
    if request.method == 'GET':
        url = "http://127.0.0.1:8000/API/get"
        header = {
          "Content-Type": "application/json",
            }

        t = requests.get(url=url, headers=header)

        trainers = {}
        trainers['main'] = 'All Trainers'
        trainers['tr'] = t.json()


        return render(request, 'allTraine.html',trainers)
def updatesv(request,id):
    if request.method == 'GET':
        ss = "http://127.0.0.1:8000/API/get/"
        url=ss+id

        header = {
            "Content-Type": "application/json",
        }

        t = requests.get(url=url, headers=header)

        trainers = {}
        trainers['main'] = 'All Trainers'
        trainers['tr'] = t.json()
        trainers['iddd'] = id



        return render(request, 'update.html',trainers)


def save(request,id):
    url = "http://127.0.0.1:8000/API/update/"
    url=url+id
    data= {
        "id": id,
        "username": request.POST['username'],
        "national": request.POST['national'],
        "fk_course":request.POST['course']
    }
    print(data)
    header = {
        "Content-Type": "application/json",
    }
    result = requests.put(url=url,data=json.dumps(data),headers=header)
    print(result)
    if result.status_code == 200:
         return HttpResponseRedirect('../all/')
    else:
        return HttpResponse('Something went wrong')


def delete(request,id):
    url = "http://127.0.0.1:8000/API/delete/"
    url = url + id


    header = {
        "Content-Type": "application/json",
    }
    result = requests.delete(url=url, headers=header)

    if result.status_code == 202:
        return HttpResponseRedirect('../all/')
    else:
        return HttpResponse('Something went wrong')

