from django import forms
from .models import *
class RegisterForm(forms.Form):
    Name=forms.CharField(label='Name',max_length=20,required=True)
    Password=forms.CharField(label='Password',max_length=12,required=True)
    Email=forms.EmailField(label='Email',max_length=50,required=True)
