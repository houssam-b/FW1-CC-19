from django.urls import path
from . import views  

urlpatterns = [
    path('about/', views.about, name='about'),
    path('all/', views.all, name='all'),
    path('collection/<int:n>', views.collection_detail, name='collection_detail'),
]