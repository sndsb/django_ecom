from django.urls import path
from .views import * 

urlpatterns = [
    path('',admin_login),
]