from django.http import HttpResponse
from adminUser.models import *


# Create your views here.

def admin_login(request):
    users = User.objects.all()
    for user in users:
        print(f'User ID: {user}')

    return HttpResponse('hello admin')
