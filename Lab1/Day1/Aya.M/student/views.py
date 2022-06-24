from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
# Create your views here.

def insert(request):
    res= HttpResponse()
    res.write('<center><h1> Hello From insert</h1></center>> ')

    return JsonResponse({'name': 'Aya', 'id': 5})
def view(request):
    res= HttpResponse()
    res.write('<center><h1> Hello, we are Students</h1></center> ')
    return res
def update(request):
    res= HttpResponse()
    res.write('<center><h1> Hello, You are in Update</h1></center> ')
    return JsonResponse({'name': 'Aya', 'id': 5})

def index(request):
    res = HttpResponse()
    res.write('<center><h1> Hello from Index </h1></center> ')
    return res

def delete(request):
    res = HttpResponse()

    return HttpResponseRedirect('../student/view')

