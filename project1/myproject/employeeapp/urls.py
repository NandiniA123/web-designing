from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployeeModelListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', EmployeeModelDetailView.as_view(), name='employee_detail'),
    path('employee/add/', EmployeeModelCreateView.as_view(), name='employee_add'),
    path('employee/<int:pk>/edit/', EmployeeModelUpdateView.as_view(), name='employee_edit'),
    path('employee/<int:pk>/delete/', EmployeeModelDeleteView.as_view(), name='employee_delete'),
]