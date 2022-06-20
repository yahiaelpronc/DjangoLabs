from django.shortcuts import render
from  django.http import HttpResponse,HttpResponseRedirect
from  .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.



def ulogin(request):
       if (request.method == 'GET'):

              if  request.session.exists(request.session.session_key):
                     t = Traine.objects.all()
                     trainers = {}
                     trainers['username'] = request.session['0']
                     trainers['tr'] = t

                     return render(request, 'users/index.html',trainers)
              else:
                     return render(request, 'users/sign-in.html')
       else:
              user = authenticate(username=request.POST['email'], password=request.POST['password'])
              if user is not None:
                     if user is not None:
                            login(request, user)
                     return HttpResponseRedirect("/admin/")


              else:
                     log = users.objects.filter(Email=request.POST['email'], password=request.POST['password'])

                     if log.exists():
                            if not request.session.exists(request.session.session_key):
                                   request.session.create()

                            context = {}
                            for e in log:
                                   z = e.firstname
                            t = Traine.objects.all()
                            trainers = {}
                            request.session[0] = z
                            trainers['username'] = z

                            trainers['tr'] = t
                            return render(request,'users/index.html',trainers)
                     else:

                            return render(request, 'users/sign-in.html')


def uregister(request):
       if (request.method == 'GET'):
              return render(request, 'users/sign-up.html')
       else:
              User.objects.create_user(username=request.POST['firstname'],email=request.POST['email'], last_name=request.POST['lastname'],  password=request.POST['password'], first_name=request.POST['firstname'],is_staff=True )
              users.objects.create(Email=request.POST['email'], lastname=request.POST['lastname'],  password=request.POST['password'], firstname=request.POST['firstname'])



              return render(request, 'index.html')

def logout_view(request):
    logout(request)

    return HttpResponseRedirect("/user/log")


