from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_buyer = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='buyer')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    residence = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """Returns a string representation of the business."""
        return self.first_name if self.first_name else 'not registered'
    

class Broker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='broker')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """Returns a string representation of the business."""
        return self.first_name if self.first_name else 'not registered'
