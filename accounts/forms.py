from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import Group


class UserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Your login', 'required': True}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Your name', 'required': True}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Your surname', 'required': True}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Your password', 'required':True}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Your password', 'required': True})

        }

