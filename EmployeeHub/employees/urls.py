from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('EmployeeListView', views.EmployeeListView, name='EmployeeListView'),
    path('EmployeeDetailView/<int:id>', views.EmployeeDetailView, name='EmployeeDetailView'),
]