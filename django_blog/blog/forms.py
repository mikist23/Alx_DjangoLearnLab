from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from .models import Post, Comment, Tag
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
    
    

# create a post form

class CreatePostForm(forms.ModelForm):
      
    tags = forms.CharField(max_length=200, required=False, help_text='Enter tags separated by commas.')
    class Meta:
        model = Post
        fields = [ 'title', 'content', 'image', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        tags = self.cleaned_data['tags']
        if commit:
            instance.save()
            instance.tags.clear()
            tag_names = [tag.strip() for tag in tags.split(',') if tag.strip()]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        return instance



# create a comment post form

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class':'form_control',
                'placeholder': 'Write a comment',
                'rows':3,
            })
        }