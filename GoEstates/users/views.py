from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import BuyerSignUpForm, BrokerSignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import User
from .decorators import buyer_required, broker_required
import django.contrib.auth.views as auth_views
from django.contrib.auth import login
from users.forms import LoginForm
from django.contrib.auth import views as auth_views



class BuyerSignUpView(CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = 'user/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('users:login')

class BrokerSignUpView(CreateView):
    model = User
    form_class = BrokerSignUpForm
    template_name = 'user/bro_reg.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'broker'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('users:login')

def Logout_view(request):
    logout(request)
    return redirect('/')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_buyer:
                return reverse('properties:home')
            elif user.is_broker:
                return reverse('broker:home')
        else:
            return reverse('user:login')
