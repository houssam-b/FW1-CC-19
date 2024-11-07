from django.urls import path
from . import views  

urlpatterns = [
    path('about/', views.about, name='about'),
    path('new/', views.new_collection, name='new_collection'),
]
