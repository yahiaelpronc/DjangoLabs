from django import forms
from .models import *
class InsertForm(forms.Form):
    name=forms.CharField(max_length=20,label='Name',required=False)
    nationalnum=forms.IntegerField(label='National Number')
    branch=forms.IntegerField(label='Branch')
    courses = forms.ChoiceField(choices=[(1, 'python'), (2, 'html'), (3, 'admin 1'), (4, 'javascript')],label='Course')
    name.widget.attrs['class']='form-control'
    nationalnum.widget.attrs['class']='form-control'
    courses.widget.attrs['class']='form-control'
    branch.widget.attrs['class']='form-control'
    #levels=forms.ChoiceField(choices=[(1,'python'),(2,'linux')])

