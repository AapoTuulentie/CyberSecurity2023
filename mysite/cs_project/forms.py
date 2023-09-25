from django import forms
from django.forms import ModelForm
from .models import User

class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]