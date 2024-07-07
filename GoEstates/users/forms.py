
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User, Buyer, Broker
from django.db import transaction
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class  BuyerSignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    residence = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Residence'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_buyer = True
        if commit:
            user.save()
        buyer = Buyer.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'),
                                     email=self.cleaned_data.get('email'),
                                     phone_number=self.cleaned_data.get('phone_number'),
                                     residence=self.cleaned_data.get('residence'),
                                     )
        return user
    

class  BrokerSignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    agency = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company or Agency'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_broker = True
        if commit:
            user.save()
        broker = Broker.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'),
                                     email=self.cleaned_data.get('email'),
                                     phone_number=self.cleaned_data.get('phone_number'),
                                     agency=self.cleaned_data.get('agency'),
                                     )
        return user

   

