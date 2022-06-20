from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json
# Create your views here.

def insert(request):
    res= HttpResponse()
    res.write('<center><h1> Hello From insert</h1></center>> ')

    return JsonResponse({'name': 'Mohamed', 'id': 50})
def view(request):
    res= HttpResponse()
    res.write('<center><h1> Helllo  From All Studnet</h1></center> ')
    return res
def update(request):
    res= HttpResponse()
    res.write('<center><h1> Hello From Update</h1></center> ')
    return JsonResponse({'name': 'Mohamed', 'id': 50})

def index(request):
    res = HttpResponse()
    res.write('<center><h1> Hello from Index </h1></center> ')
    return res

def delete(request):
    res = HttpResponse()

    return HttpResponseRedirect('../Student/view')

