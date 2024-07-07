from django.urls import path 
from .views import *


app_name = 'users'

urlpatterns = [
    path("signup/",BuyerSignUpView.as_view(), name="signup"),
    path("broker-signup/",BrokerSignUpView.as_view(), name="reg"),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', Logout_view , name='logout'),
]

   

