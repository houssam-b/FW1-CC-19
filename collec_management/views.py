from django.shortcuts import render,redirect, get_object_or_404
from .models import Collec
from .forms import CollecForm
from django.utils import timezone

#Q1

def about(request):
    return render(request,'collec_management/about.html')


#Q5

def collection_detail(request,n):
    collection=Collec.objects.get(pk=n)
    return render(request,"collec_management/collection_detail.html",{'collection':collection})



#Q6

def all(request):
    collection = Collec.objects.all()
    return render(request, 'collec_management/all.html',{'collection':collection})

#Q9

def collection_modif(request, n):
    collection = get_object_or_404(Collec, pk=n)
    if request.method == 'POST':
        form = CollecForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('all')
    else:
        form = CollecForm(instance=collection)
        
    return render(request, 'collec_management/collection_modif.html', {'form': form, 'collection': collection})

#Q7

def new_collection(request):
    if request.method == 'POST' :
        form =CollecForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.date = timezone.now()
            collection.save()
            return redirect('all')


    else :

            form=CollecForm()
            
            
            
            return render(request , 'collec_management/new_collection.html' , {'form' : form})



#Q8

def delete_collection(request,n):
    collection= Collec.objects.get(pk=n)
    if request.method == 'POST':
       collection.delete()
       return redirect('all')
    return render(request,"collec_management/delete_collection.html",{'collection':collection})