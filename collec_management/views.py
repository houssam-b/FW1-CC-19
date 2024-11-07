<<<<<<< HEAD
from django.shortcuts import render,redirect
=======

from django.shortcuts import render,redirect
from .forms import CollecForm
>>>>>>> 6e1c7d43f72cb213a0c36c47b89c09d92136def4
from .models import Collec
from django.utils import timezone

#Q1

def about(request):
    return render(request,'collec_management/about.html')


#Q7

def new_collection(request):
    if request.method == 'POST' :
        form =CollecForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.date = timezone.now()
            collection.save()
            return redirect('home')


    else :

            form=CollecForm()
            
            
            
            return render(request , 'collec_management/new_collection.html' , {'form' : form})


#Q5

def collection_detail(request,n):
    collection=Collec.objects.get(pk=n)
    return render(request,"collec_management/collection_detail.html",{'collection':collection})
<<<<<<< HEAD
#Q8
def delete_collection(request,n):
    collection= Collec.objects.get(pk=n)
    if request.method == 'POST':
       collection.delete()
       return redirect('all')
    return render(request,"collec_management/delete_collection.html",{'collection':collection})

=======



#Q6

def all(request):
    collection = Collec.objects.all()
    return render(request, 'collec_management/all.html',{'collection':collection})
>>>>>>> fc3ba3cd4ed0fabda126e463d43e785f006aedaf


