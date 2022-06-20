# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json
# Create your views here.

def liststaff(request):
    res= HttpResponse()
    res.write('<center><h1> List Staff</h1></center>> ')

    return res
def view(request):
    res= HttpResponse()
    res.write('<center><h1> Helllo  From All Studnet</h1></center> ')
    return res
def main(request):
    res= HttpResponse()
    res.write('<center><a href="../Student/view">Students</a></center> ')
    res.write('<center><a href="../Staff/view">Staffs</a></center> ')
    return res

def index(request):
    res = HttpResponse()
    res.write('<center><h1> Hello from Report Index </h1></center> ')
    return res



