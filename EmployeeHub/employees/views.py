from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee

def EmployeeListView(request):
    member = Employee.objects.all()
    context = {
        'member' : member
    }
    return render(request, 'employee_list.html', context)

def EmployeeDetailView(request,id):
    mymember = Employee.objects.get(id=id)
    context = {
        'mymember' : mymember
    }
    return render(request, 'employee_detail.html', context)

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    