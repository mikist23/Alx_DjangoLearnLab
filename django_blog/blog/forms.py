from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput,EmailInput

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=EmailInput(attrs={'placeholder':'Enter your email'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']