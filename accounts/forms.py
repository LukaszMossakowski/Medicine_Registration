from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class UserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Your login', 'required': True}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Your name', 'required': True}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Your surname', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email', 'required': True}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Your password', 'required':True}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Your password', 'required': True})
        }

class EditProfileForm(UserChangeForm):
    class Meta:
        model=User
        fields=('email', 'username', 'first_name', 'last_name')
        exclude=('password1', 'password2')
