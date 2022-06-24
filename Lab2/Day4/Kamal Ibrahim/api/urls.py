
from django.urls import path
from .views import *
urlpatterns = [
    path('/list',getData),
    path('/insert',inserttry),
    path('/delete/<pk>',delete),
    path('/update/<pk>',update)
]