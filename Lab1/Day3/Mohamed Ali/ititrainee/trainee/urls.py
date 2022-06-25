from django.urls import path,include
from .views import *
urlpatterns = [
    path('list/',list),
    path('insert/',insert),
    path('update/<id>/',update),
    path('updatetrainee/<id>/',updatetrainee ),
    path('<pk>/updategeneric/', Updategeneric.as_view()),
    path('viewdelete/',ViewDelete.as_view() ),


]