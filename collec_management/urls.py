from django.urls import path
from . import views  

urlpatterns = [
    path('about/', views.about, name='about'),
<<<<<<< HEAD
=======
    path('all/', views.all, name='all'),
>>>>>>> 47dbf5871ef33e0a7bf0ef6c029d5752bd0a199a
    path('collection/<int:n>', views.collection_detail, name='collection_detail'),
]
