
from django.shortcuts import render,redirect
from .forms import CollecForm
from .models import Collec

#Q1

def about(request):
    return render(request,'collec_management/about.html')

#Q7

def new_collection(request):
    if request.method == 'POST' :
        form =CollecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    else :

            form=CollecForm()
            
            
            
            return render(request , 'collec_management/new_collection.html' , {'form' : form})

#Q5

def collection_detail(request,n):
    collection=Collec.objects.get(pk=n)
    return render(request,"collec_management/collection_detail.html",{'collection':collection})

