from django import forms
class Myform(forms.Form):
    id=forms.IntegerField(label='id')
    name=forms.CharField(max_length=30,label='name')
    email=forms.EmailField(max_length=40,label='email')
    branch=forms.IntegerField(label='branch')
