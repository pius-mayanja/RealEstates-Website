from django.urls import path 
from .views import *


app_name = 'broker'

urlpatterns = [
    path('home/',home, name='home'),
]

   

