from django.shortcuts import render
from .models import FacultyModel
from django import forms

class FacultyForm(forms.ModelForm):
    class Meta:
        model =FacultyModel
        fields = ['name', 'department', 'email', 'mobile']
# Create your views here.
