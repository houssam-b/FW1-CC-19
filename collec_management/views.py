from django.shortcuts import render,redirect
from .models import Collec
#Q1

def about(request):
    return render(request,'collec_management/about.html')
#Q5
def collection_detail(request,n):
    collection=Collec.objects.get(pk=n)
    return render(request,"collec_management/collection_detail.html",{'collection':collection})
#Q8
def delete_collection(request,n):
    collection= Collec.objects.get(pk=n)
    if request.method == 'POST':
       collection.delete()
       return redirect('all')
    return render(request,"collec_management/delete_collection.html",{'collection':collection})


