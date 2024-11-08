from django.shortcuts import render, redirect
from .models import Collec

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
    collection = Collec.objects.get(pk=n)
    if request.method == 'POST':
        form = CollecForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('/all')
        else:
            form = CollecForm(instance=collection)
        return render(request, 'collections/collection_update.html', {'form': form, 'collection': collection})

