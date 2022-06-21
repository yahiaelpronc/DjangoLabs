from django import forms
from .models import *
class insertForm(forms.Form):
        id=forms.IntegerField(label='id',max_length=30,required=True)
        Name=forms.CharField(label='Name',max_length=20,required=True)
        Branch=forms.CharField(label='Branch',max_length=12,required=True)


