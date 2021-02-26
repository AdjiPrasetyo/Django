from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":

        username_login = request.POST['username']
        password_login = request.POST['password']
        
        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)

        return redirect(request,"dashboard")