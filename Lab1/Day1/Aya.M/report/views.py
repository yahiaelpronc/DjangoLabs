# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
# Create your views here.

def liststaff(request):
    res= HttpResponse()
    res.write('<center><h1>This is a List staff</h1></center>> ')
    return res

def view(request):
    res= HttpResponse()
    res.write('<center><h1> studentPage, Hello everyBody</h1></center> ')
    return res

def main(request):
    res= HttpResponse()
    res.write('<center><a href="../student/view">Students</a></center> ')
    res.write('<center><a href="../staff/view">Staffs</a></center> ')
    return res

def index(request):
    res = HttpResponse()
    res.write('<center><h1> Hello from report Index </h1></center> ')
    return res



