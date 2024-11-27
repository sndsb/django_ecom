from django.urls import path
from .view import product


urlpatterns = [
    path('all',product.index,name='product.index'),
    path('list',product.list,name='product.list'),
    path('add',product.add,name='product.add'),
    path('save',product.save,name='product.save'),
  
]