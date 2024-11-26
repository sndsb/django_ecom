from django.http import HttpResponse
from adminUser.models import *
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.

def admin_login(request):
    users = User.objects.all()
    for user in users:
        print(f'User ID: {user}')

    return render(request,'auth/login.html',{})
