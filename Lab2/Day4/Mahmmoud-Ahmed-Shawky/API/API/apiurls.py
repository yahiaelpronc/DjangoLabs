from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [

    path('get/', view_trainees),
    path('get/<id>', view_trainees),
    path('insert/', create_trainees),
    path('update/<pk>', update),
    path('delete/<pk>', delete),

]
