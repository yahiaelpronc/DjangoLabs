from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
import requests
from django import http

def insert(request):
        url = 'http://127.0.0.1:8000/Myapi/list'
        response = requests.get(url)
        response_data = response.json()
        print(response_data)
        context = {}
        context['outtrainne'] = response_data
        if (request.method == 'GET'):
                return render(request, 'insert.html', context)
        else:
                url = 'http://127.0.0.1:8000/Myapi/insert'
                request_data = {'id':request.POST['id'],'username':request.POST['name'],'brnach':request.POST['Branch'] }
                response = requests.post(url, json=request_data)
                if response.status_code == 200:
                        return render(request, 'insert.html', context)
                #response_data = response.json()
                else:
                        return HttpResponse('Something went wrong')
                #return http.JsonResponse(response_data)
def list(req):
        url = 'http://127.0.0.1:8000/Myapi/list'
        response = requests.get(url)
        response_data = response.json()
        context={}
        context['outtrainne']=response_data
        return render(req,'index.html',context)

def update(req,id):
        url = "http://127.0.0.1:8000/Myapi/update/"+id
        print(url)
        context1={}
        context1['id']=id
        if (req.method == 'GET'):
                return render(req,'update.html',context1)
        else :
                url = 'http://127.0.0.1:8000/Myapi/update/'+id
                request_data = {'username': req.POST['name'],
                                'brnach': req.POST['Branch']}
                response = requests.put(url, json=request_data)
                if response.status_code == 200:
                        url = 'http://127.0.0.1:8000/Myapi/list'
                        response = requests.get(url)
                        response_data = response.json()
                        context = {}
                        context['outtrainne'] = response_data
                        return render(req,'index.html', context)
                # response_data = response.json()
                else:
                        return HttpResponse('Something went wrong')
def delete(req,id):
        url = 'http://127.0.0.1:8000/Myapi/delete/'+id
        response = requests.delete(url)
        url = 'http://127.0.0.1:8000/Myapi/list'
        response = requests.get(url)
        response_data = response.json()
        context = {}
        context['outtrainne'] = response_data
        return render(req, 'index.html', context)