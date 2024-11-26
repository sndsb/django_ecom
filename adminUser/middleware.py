# myapp/middleware.py
from django.shortcuts import redirect

class GuestMiddleware:
   
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated and trying to access the login page
        if request.user.is_authenticated:
            # Redirect logged-in users away from login or register pages
            if request.path in ['/']:  # Add other guest pages if needed
                return redirect('dashboard')  # Redirect to dashboard or any other page

        response = self.get_response(request)
        return response
