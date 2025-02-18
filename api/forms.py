from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Item



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'email', 'password1', 'password2']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"