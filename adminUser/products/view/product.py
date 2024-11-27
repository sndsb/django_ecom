from django.shortcuts import render,redirect
from django.contrib import messages
from adminUser.products.model.product import Product
from django.http import JsonResponse


def index(request):
    return render(request,'products/index.html',{})

def list(request):
    
     products = Product.objects.all()
     print(products)
     return JsonResponse({'status':True})