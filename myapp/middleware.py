from django.urls import reverse
from django.shortcuts import redirect

class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            paths_to_redirect = [reverse('app:loginPage'),reverse('app:registerPage')]

            if request.path in paths_to_redirect:
                return redirect('app:landingPage')
            
        response = self.get_response(request)
        return response
    
class RestrictUnauthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_authenticated:
            paths_to_restrict = [reverse('app:dashboardPage')]

            if request.path in paths_to_restrict:
                return redirect('app:landingPage')
            
        response = self.get_response(request)
        return response