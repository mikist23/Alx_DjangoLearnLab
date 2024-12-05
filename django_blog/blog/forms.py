from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from django.forms.widgets import PasswordInput, TextInput,EmailInput

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=EmailInput(attrs={'placeholder':'Enter your email'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']

class LoginUserForm(forms.Form):
    email = forms.EmailField(widget=EmailInput())
    password = forms.CharField(widget=PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password.")
        return cleaned_data
    
    