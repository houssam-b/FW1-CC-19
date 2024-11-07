from django.urls import path
from . import views  

urlpatterns = [
    path('about/', views.about, name='about'),
<<<<<<< HEAD
    path('new/', views.new_collection, name='new_collection'),
]
=======
    path('collection/<int:n>', views.collection_detail, name='collection_detail'),
]
>>>>>>> f37b986462235dc9ee8a0866843a184a1cea1669
