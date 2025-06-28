from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import EmployeeModel
from .forms import EmployeeForm

class EmployeeModelListView(ListView):
    model = EmployeeModel
    template_name = 'employee_list.html'

class EmployeeModelDetailView(DetailView):
    model = EmployeeModel
    template_name = 'employee_detail.html'

class EmployeeModelCreateView(CreateView):
    model = EmployeeModel
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeModelUpdateView(UpdateView):
    model = EmployeeModel
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeModelDeleteView(DeleteView):
    model = EmployeeModel
    template_name = 'employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
# Create your views here.
