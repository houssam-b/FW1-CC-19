from django.shortcuts import render,redirect
from .forms import CollecForm
#Q1

def about(request):
    return render(request,'collec_management/about.html')


def new_collection(request):
    if request.method == 'POST' :
        form =CollecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    else :

            form=CollecForm()
            
            
            
            return render(request , 'collec_management/new_collection.html' , {'form' : form})