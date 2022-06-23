"""lab4apisol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('getdata/', getData ),
    path('List/',view_trainees,name='view_trainees'),
    path('create/', create_trainees, name='add-trainees'),
    path('update/<int:pk>/', update_trainees, name='update-trainees'),
    path('delete/<id>', delete, name='delete-trainees')
]
