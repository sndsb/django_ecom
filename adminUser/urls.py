from django.urls import path
from .view import auth,dashboard


urlpatterns = [
    path('',auth.admin_login,name='admin_login'),
    path('dashboard/',dashboard.dashboard,name='dashboard')
]