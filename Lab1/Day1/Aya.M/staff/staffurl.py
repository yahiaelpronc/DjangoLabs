from django.urls import path, include
from staff.views import *

urlpatterns = [

    path('view', view),
    path('insert', insert),
    path('', index),
    path('update', update),
    path('delete', delete)



]
