from django.http import HttpResponse
from adminUser.models import *
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

def guest_user_only(user):
    return not user.is_authenticated

@user_passes_test(guest_user_only, login_url='dashboard')
def admin_login(request):
   
    if request.method == 'POST' :
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.filter(username=username)
       
        if user is not None :
          
            userAuthenticate = authenticate(username=username,password=password)
            
            if  userAuthenticate :
                
                login(request, userAuthenticate)
                
                messages.success(request,'User logged in successfully')
                return redirect('dashboard')
            else:
                messages.error(request,'invalid credentials')
                return redirect('admin_login')
        else:
            messages.error(request,'User is not registerd')
            return redirect('admin_login')
    else:
      return render(request,'auth/login.html',{})
  
