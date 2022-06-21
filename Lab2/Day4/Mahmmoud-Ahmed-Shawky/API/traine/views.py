from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import render
from .forms import InputForm

from users.models import *
# Create your views here.
def insert(request):
      if (request.method == 'GET'):
             context = {}
             context['form'] = InputForm()
             context['username'] = request.session['0']

             return render(request, 'traine/insert.html',context)
      else:

            context = {}
            Traine.objects.create(username=request.POST['username'], national=request.POST['national'],fk_course=Courses.objects.get(Course_id=request.POST['Courses']))
            context['username'] = request.session['0']
            return render(request, 'users/index.html',context)




def home(request):
   context = {}
   context['username'] = request.session['0']
   if request.method=='POST':
      form=InputForm(request.POST)
      if form.is_valid():
         form.save()
         return render(request, 'users/index.html', context)








class cView(CreateView):
    model = Traine
    fields = ['username','national','fk_course']
    template_name = "traine/update.html"


class uView(UpdateView):
    model = Traine
    fields = ['username','national','fk_course']
    template_name = "traine/update.html"
    success_url = "../../user/log/"


class dView(DeleteView):
    model = Traine
    template_name = "traine/del.html"
    fields = ['username','national','fk_course']
    success_url = "../../user/log/"




