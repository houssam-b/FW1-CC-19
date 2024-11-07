from django.shortcuts import render
from .models import Collec

#Q1

def about(request):
    return render(request,'collec_management/about.html')

#Q6

def all(request):
    collection = Collec.objects.all()
    return render(request, 'collec_management/all.html',{'collection':collection})
