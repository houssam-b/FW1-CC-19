from django.urls import path
from . import views  

urlpatterns = [
    path('about/', views.about, name='about'),
]
urlpatterns = [
    path('collection/<int:n>', views.collection_detail, name='collection_detail'),
]