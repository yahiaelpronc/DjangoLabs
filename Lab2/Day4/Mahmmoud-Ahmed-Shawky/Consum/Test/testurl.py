from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [

    path('get/',getTest),
    path('get/<id>',getTest),
    path('post/',postTest),
    path('all/', updateTestv),
    path('update/<id>', updatesv),
    path('save/<id>', save),
    path('delete/<id>', delete)

]
