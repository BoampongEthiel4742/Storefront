from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from django import forms

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','password']



  

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address...',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password...',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username...',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address...',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password...',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'confirm password...',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','price','description','image']


