from django import forms
from .models import *
class updateForm(forms.Form):
        Name=forms.CharField(label='Name',max_length=20,required=True)
        Branch=forms.CharField(label='Branch',max_length=12,required=True)
        NationalNumber=forms.CharField(label='NationalNumber',max_length=50,required=True)
        Course=forms.CharField(label='Course',max_length=20,required=True)


