from django.urls import path

from django.urls import path, include
from student.views import *
urlpatterns = [

    path('view', view),
    path('insert', insert),
    path('', index),
    path('update', update),
    path('delete',delete)


]
