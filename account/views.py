from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import CreateView
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.views import LoginView


# Create your views here.
class UserRegister(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return self.request.GET.get('next') or '/'


def logout(request):
    auth_logout(request)
    return redirect('index')