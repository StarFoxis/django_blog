from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class MyLoginView(LoginView):
    template_name = 'login.html'

class MyLogoutView(LogoutView):
    # template_name = 'logout.html'
    pass

def profile(request):
    return render(request, 'profile.html')