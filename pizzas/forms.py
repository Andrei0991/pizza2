from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
class SizeForm(ModelForm):
     class Meta:
        model = Order_product
        fields = ('size', 'product')
        widgets = {'product': forms.HiddenInput()}


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')