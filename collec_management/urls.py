from django.urls import path
from . import views  

urlpatterns = [
    path('about/', views.about, name='about'),
    path('collection/<int:n>', views.collection_detail, name='collection_detail'),
    path('delete/<int:n>', views.delete_collection, name='delete_collection'),
    path('new/', views.new_collection, name='new_collection'),
    path('all/', views.all, name='all'),
]

