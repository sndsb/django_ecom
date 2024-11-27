from django.urls import path
from .view import product


urlpatterns = [
    path('product/',product.index,name='product.index'),
    path('product_list/',product.list,name='product.list'),
  
]