from django.urls import path
from .views import *

app_name = 'properties'


urlpatterns = [
    path('',homepage, name='home'),
    path('our-properties/',properties, name='property'),
    path('detail/<pk>',details, name='details'),
    path('video/<pk>',vid, name='vid'),
]