from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse

#mployee.objects.all()


def funcselect(request):
    q = Employee.objects.all()
    return render(request,'output.html', {'members':q}) 
    # return HttpResponse('hello')