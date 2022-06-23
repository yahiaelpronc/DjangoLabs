from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .forms import Myform
# Create your views here.
from django.http import HttpResponse

import requests
def callgetmethod(req):
    if (req.method == "GET"):
        context = {}
        context['form'] = Myform
        return render(req, 'index.html', context)
    else:

        url = "http://127.0.0.1:8000/trainee/create/"
        header = {"Content-Type": "application/json"}
        data = {'id': req.POST["id"], 'name': req.POST['name'],'email':req.POST['email']}
        result = requests.post(url=url, data=json.dumps(data), headers=header)
        if result.status_code == 200:
            return HttpResponse('Successful')
        else:
            return HttpResponse('Something went wrong')


def callpostmethod(req):
    pass

def list(req):
    url="http://127.0.0.1:8000/trainee/List/"
    header = {"Content-Type": "application/json"}
    result=requests.get(url=url)
    data=result.json()
    context = {}
    context['data'] = data
    return render(req, 'list.html', context)


def delete(req,id):
    url = "http://127.0.0.1:8000/trainee/delete/"+id
    result = requests.delete(url=url)
    url = "http://127.0.0.1:8000/trainee/List/"
    header = {"Content-Type": "application/json"}
    result = requests.get(url=url)
    data = result.json()
    context = {}
    context['data'] = data
    return render(req, 'list.html', context)

def update(req,id):
    url= "http://127.0.0.1:8000/trainee/update/"+id
    header = {"Content-Type": "application/json"}
    result = requests.get(url=url)
    data = result.json()
    context = {}
    context['data'] = data
    return render(req, 'list.html', context)