from django.shortcuts import render
from .models import EmployeeModel
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model =EmployeeModel
        fields = ['name','email', 'department']
# Create your views here.
