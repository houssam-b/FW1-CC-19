from django.shortcuts import render,redirect
from .models import Collec

#Q1

def about(request):
    return render(request,'collec_management/about.html')

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

