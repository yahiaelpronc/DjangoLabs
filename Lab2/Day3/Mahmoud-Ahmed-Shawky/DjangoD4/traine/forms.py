
from django import forms
from users.models import *


class InputForm(forms.Form):
    c = Courses.objects.all()
    final_choices = []
    for course in c:
        CHOICES = ()
        CHOICES = (course.Course_id, course.Cours_Name)
        final_choices.append(CHOICES)

    CHOICES = tuple(final_choices)
    username = forms.CharField(max_length=200)
    national = forms.CharField(max_length=200)
    Courses = forms.ChoiceField(choices=CHOICES)



