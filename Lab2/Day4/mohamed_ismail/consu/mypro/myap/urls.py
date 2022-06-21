from django.urls import path
from .views import *
urlpatterns = [
    path('/list',list),
    path('/insert',insert),
    path('/update/<id>',update),
    path('/delete/<id>',delete),
]