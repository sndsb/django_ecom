from django.urls import path
from .view import product


urlpatterns = [
    path('product/',product.index,name='product.index'),
  
]