from django.shortcuts import render
from .models import Collec
#Q1

def about(request):
    return render(request,'collec_management/about.html')
#Q5
def collection_detail(request,n):
    collection=Collec.objects.get(pk=n)
    return render(request,"collec_management/collection_detail.html",{'collection':collection})