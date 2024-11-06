from django.shortcuts import render

#Q1

def about(request):
    return render(request,'collec_management/about.html')
