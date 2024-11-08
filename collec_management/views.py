from django.shortcuts import render,redirect
from .forms import CollecForm
from .models import Collec
from django.utils import timezone

#Q1

def about(request):
    return render(request,'collec_management/about.html')


<<<<<<< HEAD

=======
>>>>>>> dev
#Q5

def collection_detail(request,n):
    collection=Collec.objects.get(pk=n)
    return render(request,"collec_management/collection_detail.html",{'collection':collection})



#Q6

def all(request):
    collection = Collec.objects.all()
    return render(request, 'collec_management/all.html',{'collection':collection})

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
