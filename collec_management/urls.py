from django.urls import path
from . import views  

urlpatterns = [
    path('about/', views.about, name='about'),
<<<<<<< HEAD
=======
    path('all/', views.all, name='all'),
>>>>>>> fc3ba3cd4ed0fabda126e463d43e785f006aedaf
    path('collection/<int:n>', views.collection_detail, name='collection_detail'),
    path('delete/<int:n>', views.delete_collection, name='delete_collection'),
]

    
