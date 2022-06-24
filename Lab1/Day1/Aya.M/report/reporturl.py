from django.urls import path, include
from report.views import *
urlpatterns = [

    path('view', view),
    path('list', liststaff),
    path('', index),
    path('mainreport', main),



]
